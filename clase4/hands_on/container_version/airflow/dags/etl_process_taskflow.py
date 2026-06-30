import datetime

from airflow.decorators import dag, task

default_args = {
    "depends_on_past": False,
    "schedule_interval": None,
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=5),
    "dagrun_timeout": datetime.timedelta(minutes=15),
}


@dag(
    dag_id="etl_with_taskflow",
    description="Proceso ETL de ejemplo usando TaskFlow",
    default_args=default_args,
    catchup=False,
    tags=["ETL", "TaskFlow"],
)
def process_etl_taskflow():  # noqa: PLR0915

    @task.virtualenv(
        task_id="obtain_original_data",
        requirements=["ucimlrepo>=0.0"],
        system_site_packages=False,
    )
    def get_data():
        """
        Carga los datos desde de la fuente
        """
        from ucimlrepo import fetch_ucirepo  # noqa: PLC0415

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
        system_site_packages=False,
    )
    def make_dummies_variables(path_input):
        """
        Convierte a las variables en Dummies
        """
        import pandas as pd  # noqa: PLC0415

        print(f"📂 Leyendo archivo: {path_input}")
        dataset = pd.read_csv(path_input)

        print("🧼 Eliminando duplicados y nulos...")
        dataset.drop_duplicates(inplace=True, ignore_index=True)
        dataset.dropna(inplace=True, ignore_index=True)

        print("🔄 Convertiendo columnas categóricas a enteros...")
        for col in ["cp", "restecg", "slope", "ca", "thal"]:
            dataset[col] = dataset[col].astype(int)

        print("🏷️ Generando variables dummy...")
        dataset_with_dummies = pd.get_dummies(
            dataset, columns=["cp", "restecg", "slope", "ca", "thal"], drop_first=True
        )

        output_path = "./data_clean_dummies.csv"
        dataset_with_dummies.to_csv(output_path, index=False)
        print(f"💾 Dataset limpio guardado en: {output_path}")

        # Enviamos dos mensajes entre nodo
        # OBS: Recordad que no se mandan mucha información, solo mensajes de
        # comunicación. Si querés pasar dataset entre nodos, es mejor guardar
        # en algún lado y pasar el path o similar.
        return {
            "path": output_path,
            "observations": dataset_with_dummies.shape[0],
            "columns": dataset_with_dummies.shape[1],
        }

    @task.virtualenv(
        task_id="split_dataset",
        requirements=["pandas>=2.0", "scikit-learn>=1.3.2"],
        multiple_outputs=True,
        system_site_packages=False,
    )
    def split_dataset(file_path, obs, col):
        """
        Genera el dataset y obtiene set de testeo y evaluación
        """
        import pandas as pd  # noqa: PLC0415
        from sklearn.model_selection import train_test_split  # noqa: PLC0415

        df = pd.read_csv(file_path)
        assert df.shape == (obs, col), (
            "⚠️ La forma del dataset no coincide con lo esperado."
        )

        print("🔀 Separando dataset en entrenamiento y prueba...")
        xx = df.drop(columns="num")
        y = df["num"]

        xx_train, xx_test, y_train, y_test = train_test_split(
            xx, y, test_size=0.3, stratify=y
        )

        xx_train_path = "./X_train.csv"
        y_train_path = "./y_train.csv"
        xx_test_path = "./X_test.csv"
        y_test_path = "./y_test.csv"

        xx_train.to_csv(xx_train_path, index=False)
        xx_test.to_csv(xx_test_path, index=False)
        y_train.to_csv(y_train_path, index=False)
        y_test.to_csv(y_test_path, index=False)
        print("✅ Datos de entrenamiento y prueba guardados.")

        return {
            "xx_train_file_path": xx_train_path,
            "y_train_file_path": y_train_path,
            "xx_test_file_path": xx_test_path,
            "y_test_file_path": y_test_path,
        }

    @task.virtualenv(
        task_id="normalize_numerical_features",
        requirements=["pandas>=2.3", "scikit-learn>=1.3.2"],
        multiple_outputs=True,
        system_site_packages=False,
    )
    def normalize_data(xx_train_path, xx_test_path):
        """
        Estandarizamos los datos
        """
        import pandas as pd  # noqa: PLC0415
        from sklearn.preprocessing import StandardScaler  # noqa: PLC0415

        print("🔢 Leyendo datos para normalizar...")
        xx_train = pd.read_csv(xx_train_path)
        xx_test = pd.read_csv(xx_test_path)

        print("📏 Estandarizando variables numéricas...")
        scaler = StandardScaler()
        xx_train_scaled = scaler.fit_transform(xx_train)
        xx_test_scaled = scaler.transform(xx_test)

        xx_train_norm_path = "./X_train_norm.csv"
        xx_test_norm_path = "./X_test_norm.csv"

        pd.DataFrame(xx_train_scaled, columns=xx_train.columns).to_csv(
            xx_train_norm_path, index=False
        )
        pd.DataFrame(xx_test_scaled, columns=xx_test.columns).to_csv(
            xx_test_norm_path, index=False
        )

        print("✅ Datos normalizados y guardados.")
        return {
            "xx_train_file_path": xx_train_norm_path,
            "xx_test_file_path": xx_test_norm_path,
        }

    @task.virtualenv(
        task_id="read_train_data",
        requirements=["pandas>=2.3"],
        system_site_packages=False,
    )
    def read_train_data(xx_train_path, y_train_path):
        """
        Leemos los datos de entrenamiento
        """
        import pandas as pd  # noqa: PLC0415

        xx_train = pd.read_csv(xx_train_path)
        y_train = pd.read_csv(y_train_path)
        print(f"📚 Datos de entrenamiento: X={xx_train.shape}, y={y_train.shape}")

    @task.virtualenv(
        task_id="read_test_data",
        requirements=["pandas>=2.3"],
        system_site_packages=False,
    )
    def read_test_data(xx_test_path, y_test_path):
        """
        Leemos los datos de testeo
        """
        import pandas as pd  # noqa: PLC0415

        xx_test = pd.read_csv(xx_test_path)
        y_test = pd.read_csv(y_test_path)
        print(f"🧪 Datos de testeo: X={xx_test.shape}, y={y_test.shape}")

    # 🧩 Encadenamiento
    path = get_data()
    dims = make_dummies_variables(path)
    files = split_dataset(dims["path"], dims["observations"], dims["columns"])
    files_norm = normalize_data(files["xx_train_file_path"], files["xx_test_file_path"])
    read_train_data(files_norm["xx_train_file_path"], files["y_train_file_path"])
    read_test_data(files_norm["xx_test_file_path"], files["y_test_file_path"])


dag = process_etl_taskflow()
