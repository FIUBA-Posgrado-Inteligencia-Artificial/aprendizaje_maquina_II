import datetime
from airflow.decorators import dag, task

default_args = {
    'depends_on_past': False,
    'schedule_interval': None,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
    'dagrun_timeout': datetime.timedelta(minutes=15)
}


@dag(
    dag_id="etl_with_taskflow",
    description="Proceso ETL de ejemplo usando TaskFlow",
    default_args=default_args,
    catchup=False,
    tags=["ETL", "TaskFlow"],
)
def process_etl_taskflow():

    @task.virtualenv(
        task_id="obtain_original_data",
        requirements=["ucimlrepo>=0.0"],
        system_site_packages=False
    )
    def get_data():
        """
        Carga los datos desde de la fuente
        """
        from ucimlrepo import fetch_ucirepo

        # Obtenemos el dataset
        print("📥 Descargando dataset de UCIML...")
        dataset = fetch_ucirepo(id=45).data.original

        print("🧹 Normalizando columna 'num'...")
        dataset.loc[dataset["num"] > 0, "num"] = 1

        path = "./data.csv"
        dataset.to_csv(path, index=False)
        print(f"💾 Dataset guardado en: {path}")

        # Enviamos un mensaje para el siguiente nodo
        return path

    @task.virtualenv(
        task_id="make_dummies_variables",
        multiple_outputs=True,
        requirements=["pandas>=2.0"],
        system_site_packages=False
    )
    def make_dummies_variables(path_input):
        """
        Convierte a las variables en Dummies
        """
        import pandas as pd

        print(f"📂 Leyendo archivo: {path_input}")
        dataset = pd.read_csv(path_input)

        print("🧼 Eliminando duplicados y nulos...")
        dataset.drop_duplicates(inplace=True, ignore_index=True)
        dataset.dropna(inplace=True, ignore_index=True)

        print("🔄 Convertiendo columnas categóricas a enteros...")
        for col in ["cp", "restecg", "slope", "ca", "thal"]:
            dataset[col] = dataset[col].astype(int)

        print("🏷️ Generando variables dummy...")
        dataset_with_dummies = pd.get_dummies(dataset,
                                              columns=["cp", "restecg", "slope", "ca", "thal"],
                                              drop_first=True)


        output_path = "./data_clean_dummies.csv"
        dataset_with_dummies.to_csv(output_path, index=False)
        print(f"💾 Dataset limpio guardado en: {output_path}")

        # Enviamos dos mensajes entre nodo
        # OBS: Recordad que no se mandan mucha información, solo mensajes de comunicación. Si querés pasar dataset
        # entre nodos, es mejor guardar en algún lado y pasar el path o similar.
        return {
            "path": output_path,
            "observations": dataset_with_dummies.shape[0],
            "columns": dataset_with_dummies.shape[1]
        }


    @task.virtualenv(
        task_id="split_dataset",
        requirements=["pandas>=2.0",
                      "scikit-learn>=1.3.2"],
        multiple_outputs=True,
        system_site_packages=False
    )
    def split_dataset(file_path, obs, col):
        """
        Genera el dataset y obtiene set de testeo y evaluación
        """
        import pandas as pd
        from sklearn.model_selection import train_test_split

        df = pd.read_csv(file_path)
        assert df.shape == (obs, col), "⚠️ La forma del dataset no coincide con lo esperado."

        print("🔀 Separando dataset en entrenamiento y prueba...")
        X = df.drop(columns="num")
        y = df["num"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

        X_train_path = "./X_train.csv"
        y_train_path = "./y_train.csv"
        X_test_path = "./X_test.csv"
        y_test_path = "./y_test.csv"

        X_train.to_csv(X_train_path, index=False)
        X_test.to_csv(X_test_path, index=False)
        y_train.to_csv(y_train_path, index=False)
        y_test.to_csv(y_test_path, index=False)
        print("✅ Datos de entrenamiento y prueba guardados.")

        return {
            "X_train_file_path": X_train_path,
            "y_train_file_path": y_train_path,
            "X_test_file_path": X_test_path,
            "y_test_file_path": y_test_path,
        }


    @task.virtualenv(
        task_id="normalize_numerical_features",
        requirements=["pandas>=2.3",
                      "scikit-learn>=1.3.2"],
        multiple_outputs=True,
        system_site_packages=False
    )
    def normalize_data(X_train_path, X_test_path):
        """
        Estandarizamos los datos
        """
        import pandas as pd
        from sklearn.preprocessing import StandardScaler

        print("🔢 Leyendo datos para normalizar...")
        X_train = pd.read_csv(X_train_path)
        X_test = pd.read_csv(X_test_path)

        print("📏 Estandarizando variables numéricas...")
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        X_train_norm_path = "./X_train_norm.csv"
        X_test_norm_path = "./X_test_norm.csv"

        pd.DataFrame(X_train_scaled, columns=X_train.columns).to_csv(X_train_norm_path, index=False)
        pd.DataFrame(X_test_scaled, columns=X_test.columns).to_csv(X_test_norm_path, index=False)

        print("✅ Datos normalizados y guardados.")
        return {
            "X_train_file_path": X_train_norm_path,
            "X_test_file_path": X_test_norm_path
        }

    @task.virtualenv(
        task_id="read_train_data",
        requirements=["pandas>=2.3"],
        system_site_packages=False
    )
    def read_train_data(X_train_path, y_train_path):
        """
        Leemos los datos de entrenamiento
        """
        import pandas as pd
        X_train = pd.read_csv(X_train_path)
        y_train = pd.read_csv(y_train_path)
        print(f"📚 Datos de entrenamiento: X={X_train.shape}, y={y_train.shape}")

    @task.virtualenv(
        task_id="read_test_data",
        requirements=["pandas>=2.3"],
        system_site_packages=False
    )
    def read_test_data(X_test_path, y_test_path):
        """
        Leemos los datos de testeo
        """
        import pandas as pd
        X_test = pd.read_csv(X_test_path)
        y_test = pd.read_csv(y_test_path)
        print(f"🧪 Datos de testeo: X={X_test.shape}, y={y_test.shape}")


    # 🧩 Encadenamiento
    path = get_data()
    dims = make_dummies_variables(path)
    files = split_dataset(dims["path"], dims["observations"], dims["columns"])
    files_norm = normalize_data(files["X_train_file_path"], files["X_test_file_path"])
    read_train_data(files_norm["X_train_file_path"], files["y_train_file_path"])
    read_test_data(files_norm["X_test_file_path"], files["y_test_file_path"])

dag = process_etl_taskflow()
