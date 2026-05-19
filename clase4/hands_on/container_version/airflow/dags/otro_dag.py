from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
}

@dag(
    schedule="*/30 * * * *",
    start_date=datetime(2026,1,1),
    catchup=False,
    tags=["clase4"],
    default_args=default_args,
    params={
        "test_size": 0.3,
        "min_accuracy": 0.80,
        "step_delay": 30
    }
)
def otro_dag():

    @task(task_id="el_primer_paso")
    def otro_task(delay):
        import time

        print("hola, mundo, este es otro DAG")
        time.sleep(int(delay))

    @task.virtualenv(
        task_id="descarga_dataset",
        requirements=["ucimlrepo", "pandas", "boto3"])
    def get_data(delay):
        import io
        import time
        import uuid
        import boto3
        from ucimlrepo import fetch_ucirepo

        bucket = "data"

        print("📥 Descargando dataset de UCIML...")
        dataset = fetch_ucirepo(id=45).data.original

        print("🧹 Normalizando columna 'num'...")
        dataset.loc[dataset["num"] > 0, "num"] = 1

        key = f"raw/data_{uuid.uuid4().hex}.csv"
        buf = io.StringIO()
        dataset.to_csv(buf, index=False)
        boto3.client("s3").put_object(Bucket=bucket, Key=key, Body=buf.getvalue())

        s3_path = f"s3://{bucket}/{key}"
        print(f"💾 Dataset guardado en: {s3_path}")

        time.sleep(int(delay))
        return s3_path

    @task.virtualenv(
        task_id="procesar_datos",
        multiple_outputs=True,
        python_version="3.10",
        requirements=["pandas>=2.0", "boto3"])
    def process_data(s3_path, delay):
        import io
        import time
        import uuid
        import boto3
        import pandas as pd

        bucket = "data"
        s3 = boto3.client("s3")

        print(f"📂 Cargando dataset desde: {s3_path}")
        in_bucket, in_key = s3_path.replace("s3://", "").split("/", 1)
        obj = s3.get_object(Bucket=in_bucket, Key=in_key)
        df = pd.read_csv(io.BytesIO(obj["Body"].read()))

        df.drop_duplicates(inplace=True, ignore_index=True)
        df.dropna(inplace=True, ignore_index=True)

        for col in ["cp", "restecg", "slope", "ca", "thal"]:
            df[col] = df[col].astype(int)

        df_with_dummies = pd.get_dummies(df,
                            columns=["cp", "restecg", "slope", "ca", "thal"],
                            drop_first=True)

        out_key = f"processed/data_clean_dummies_{uuid.uuid4().hex}.csv"
        buf = io.StringIO()
        df_with_dummies.to_csv(buf, index=False)
        s3.put_object(Bucket=bucket, Key=out_key, Body=buf.getvalue())

        out_path = f"s3://{bucket}/{out_key}"
        print(f"💾 Dataset limpio guardado en: {out_path}")
        time.sleep(int(delay))

        return {
            "path": out_path,
            "observations": df_with_dummies.shape[0],
            "columns": df_with_dummies.shape[1]
        }

    @task.virtualenv(
        task_id="split_dataset",
        requirements=["pandas",
                      "scikit-learn",
                      "boto3"],
        multiple_outputs=True,
        system_site_packages=False
    )
    def split_dataset(file_path, obs, col, test_size, delay):
        import io
        import time
        import uuid
        import boto3
        import pandas as pd
        from sklearn.model_selection import train_test_split

        bucket = "data"
        s3 = boto3.client("s3")

        test_size = float(test_size)

        in_bucket, in_key = file_path.replace("s3://", "").split("/", 1)
        obj = s3.get_object(Bucket=in_bucket, Key=in_key)
        df = pd.read_csv(io.BytesIO(obj["Body"].read()))
        assert df.shape == (obs, col), "⚠️ La forma del dataset no coincide con lo esperado."

        print("🔀 Separando dataset en entrenamiento y prueba...")
        X = df.drop(columns="num")
        y = df["num"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, stratify=y)

        unique_id = uuid.uuid4().hex
        outputs = {
            "X_train_file_path": (X_train, f"splits/X_train_{unique_id}.csv"),
            "y_train_file_path": (y_train, f"splits/y_train_{unique_id}.csv"),
            "X_test_file_path": (X_test, f"splits/X_test_{unique_id}.csv"),
            "y_test_file_path": (y_test, f"splits/y_test_{unique_id}.csv"),
        }

        paths = {}
        for name, (data, key) in outputs.items():
            buf = io.StringIO()
            data.to_csv(buf, index=False)
            s3.put_object(Bucket=bucket, Key=key, Body=buf.getvalue())
            paths[name] = f"s3://{bucket}/{key}"

        print("✅ Datos de entrenamiento y prueba guardados.")
        time.sleep(int(delay))

        return paths


    @task.virtualenv(
        task_id="normalize_numerical_features",
        requirements=["pandas>=2.3",
                      "scikit-learn>=1.3.2",
                      "boto3"],
        multiple_outputs=True,
        system_site_packages=False
    )
    def normalize_data(X_train_path, X_test_path, delay):
        import io
        import time
        import uuid
        import boto3
        import pandas as pd
        from sklearn.preprocessing import StandardScaler

        bucket = "data"
        s3 = boto3.client("s3")

        def _read(path):
            b, k = path.replace("s3://", "").split("/", 1)
            obj = s3.get_object(Bucket=b, Key=k)
            return pd.read_csv(io.BytesIO(obj["Body"].read()))

        print("🔢 Leyendo datos para normalizar...")
        X_train = _read(X_train_path)
        X_test = _read(X_test_path)

        print("📏 Estandarizando variables numéricas...")
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        unique_id = uuid.uuid4().hex
        out_train_key = f"normalized/X_train_norm_{unique_id}.csv"
        out_test_key = f"normalized/X_test_norm_{unique_id}.csv"

        for data, cols, key in [
            (X_train_scaled, X_train.columns, out_train_key),
            (X_test_scaled, X_test.columns, out_test_key),
        ]:
            buf = io.StringIO()
            pd.DataFrame(data, columns=cols).to_csv(buf, index=False)
            s3.put_object(Bucket=bucket, Key=key, Body=buf.getvalue())

        print("✅ Datos normalizados y guardados.")
        time.sleep(int(delay))
        return {
            "X_train_file_path": f"s3://{bucket}/{out_train_key}",
            "X_test_file_path": f"s3://{bucket}/{out_test_key}",
        }

    @task.virtualenv(
        task_id="train_model",
        requirements=["pandas", "scikit-learn", "joblib", "boto3"],
        system_site_packages=False,
    )
    def train_model(X_train_path, y_train_path, delay):
        import io
        import time
        import uuid
        import boto3
        import joblib
        import pandas as pd
        from sklearn.linear_model import LogisticRegression

        bucket = "data"
        s3 = boto3.client("s3")

        def _read(path):
            b, k = path.replace("s3://", "").split("/", 1)
            obj = s3.get_object(Bucket=b, Key=k)
            return pd.read_csv(io.BytesIO(obj["Body"].read()))

        X_train = _read(X_train_path)
        y_train = _read(y_train_path)

        model = LogisticRegression()
        model.fit(X_train, y_train)

        key = f"models/model_{uuid.uuid4().hex}.pkl"
        buf = io.BytesIO()
        joblib.dump(model, buf)
        buf.seek(0)
        s3.put_object(Bucket=bucket, Key=key, Body=buf.getvalue())

        time.sleep(int(delay))
        return f"s3://{bucket}/{key}"

    @task.virtualenv(
        task_id="test_model",
        requirements=["pandas", "scikit-learn", "joblib", "boto3"],
        multiple_outputs=True,
        system_site_packages=False
    )
    def test_model(X_test_path, y_test_path, model_path, delay):
        import io
        import time
        import boto3
        import joblib
        import pandas as pd

        s3 = boto3.client("s3")

        def _read_csv(path):
            b, k = path.replace("s3://", "").split("/", 1)
            obj = s3.get_object(Bucket=b, Key=k)
            return pd.read_csv(io.BytesIO(obj["Body"].read()))

        b, k = model_path.replace("s3://", "").split("/", 1)
        model_obj = s3.get_object(Bucket=b, Key=k)
        model = joblib.load(io.BytesIO(model_obj["Body"].read()))

        X_test = _read_csv(X_test_path)
        y_test = _read_csv(y_test_path)

        accuracy = model.score(X_test, y_test)

        print(f"✅ Accuracy del modelo en testeo: {accuracy:.4f}")
        time.sleep(int(delay))

        return {"accuracy": accuracy}

    @task.branch(task_id="evaluar_modelo")
    def check_accuracy(accuracy: float, min_accuracy: str):
        if accuracy >= float(min_accuracy):
            return "deploy_model"
        return "do_nothing"

    @task.virtualenv(
        task_id="deploy_model",
        requirements=["boto3"]
    )
    def deploy_model(model_path, delay):
        import time
        import boto3

        bucket = "data"
        prod_prefix = "production/"
        prod_key = f"{prod_prefix}model.pkl"

        s3 = boto3.client("s3")

        print(f"🧹 Buscando modelos previos en s3://{bucket}/{prod_prefix}...")
        existing = s3.list_objects_v2(Bucket=bucket, Prefix=prod_prefix)
        if "Contents" in existing:
            to_delete = [{"Key": obj["Key"]} for obj in existing["Contents"]]
            s3.delete_objects(Bucket=bucket, Delete={"Objects": to_delete})
            for obj in to_delete:
                print(f"🗑️ Eliminado modelo previo: s3://{bucket}/{obj['Key']}")
        else:
            print("ℹ️ No había modelo previo en producción.")

        src_bucket, src_key = model_path.replace("s3://", "").split("/", 1)
        s3.copy_object(
            Bucket=bucket,
            Key=prod_key,
            CopySource={"Bucket": src_bucket, "Key": src_key}
        )
        time.sleep(int(delay))
        print(f"🚀 Modelo desplegado en: s3://{bucket}/{prod_key}")

    @task(task_id="do_nothing")
    def do_nothing(delay):
        import time
        print("🛑 El modelo no superó el umbral mínimo. No se hace nada.")
        time.sleep(int(delay))

    @task.virtualenv(
        task_id="cleanup_files",
        trigger_rule="all_done",
        requirements=["boto3"]
    )
    def cleanup_files(*paths):
        import boto3
        s3 = boto3.client("s3")
        print("🧹 Limpiando objetos en S3...")
        for path in paths:
            if isinstance(path, str) and path.startswith("s3://"):
                bucket, key = path.replace("s3://", "").split("/", 1)
                try:
                    s3.delete_object(Bucket=bucket, Key=key)
                    print(f"🗑️ Eliminado: {path}")
                except Exception as e:
                    print(f"⚠️ Error eliminando {path}: {e}")


    delay = "{{ params.step_delay }}"

    path = get_data(delay) # Cada vez que se llama una función decorada con @task, se genera un objeto Task
    otro_task(delay) >> path
    data = process_data(path, delay)

    # Pasamos el test_size desde los params del DAG
    files = split_dataset(data["path"], data["observations"], data["columns"], "{{ params.test_size }}", delay)
    norm_files = normalize_data(files["X_train_file_path"], files["X_test_file_path"], delay)
    training_artifact = train_model(norm_files["X_train_file_path"], files["y_train_file_path"], delay)
    test_results = test_model(norm_files["X_test_file_path"], files["y_test_file_path"], training_artifact, delay)

    # Lógica de Branching
    eval_step = check_accuracy(test_results["accuracy"], "{{ params.min_accuracy }}")
    deploy = deploy_model(training_artifact, delay)
    do_not = do_nothing(delay)

    eval_step >> [deploy, do_not]

    # Lógica de Limpieza al final (se ejecuta sin importar qué camino tomó el branch)
    limpieza = cleanup_files(
        path,
        data["path"],
        files["X_train_file_path"], files["y_train_file_path"],
        files["X_test_file_path"], files["y_test_file_path"],
        norm_files["X_train_file_path"], norm_files["X_test_file_path"],
        training_artifact,
    )

    deploy >> limpieza
    do_not >> limpieza

dag = otro_dag()
