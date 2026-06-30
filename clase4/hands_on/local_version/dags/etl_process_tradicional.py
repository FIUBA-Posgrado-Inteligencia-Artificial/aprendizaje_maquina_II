import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import (
    PythonVirtualenvOperator,  # It will be deprecated soon
)
from pendulum import today

default_args = {
    "depends_on_past": False,
    "schedule_interval": None,
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=5),
    "dagrun_timeout": datetime.timedelta(minutes=15),
}

dag = DAG(
    "etl_without_taskflow",
    default_args=default_args,
    description="Proceso ETL de ejemplo sin TaskFlow",
    start_date=today("UTC").subtract(days=2),
    tags=["ETL"],
)


def obtain_original_data():
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
    # comunicación. Si querés pasar dataset entre nodos, es mejor guardar en
    # algún lado y pasar el path o similar.
    return {
        "path": output_path,
        "observations": dataset_with_dummies.shape[0],
        "columns": dataset_with_dummies.shape[1],
    }


def split_dataset(shape_input_ast):
    """
    Genera el dataset y obtiene set de testeo y evaluación
    """
    import ast  # noqa: PLC0415

    import pandas as pd  # noqa: PLC0415
    from sklearn.model_selection import train_test_split  # noqa: PLC0415

    input_data = ast.literal_eval(shape_input_ast)
    path = input_data["path"]
    observations = input_data["observations"]
    columns = input_data["columns"]

    df = pd.read_csv(path)
    assert df.shape == (observations, columns), (
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


def normalize_data(file_dict_ast):
    """
    Estandarizamos los datos
    """
    import ast  # noqa: PLC0415

    import pandas as pd  # noqa: PLC0415
    from sklearn.preprocessing import StandardScaler  # noqa: PLC0415

    input_data = ast.literal_eval(file_dict_ast)
    xx_train_path = input_data["xx_train_file_path"]
    xx_test_path = input_data["xx_test_file_path"]
    y_train_path = input_data["y_train_file_path"]
    y_test_path = input_data["y_test_file_path"]

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
        "./X_train.csv", index=False
    )
    pd.DataFrame(xx_test_scaled, columns=xx_test.columns).to_csv(
        "./X_test.csv", index=False
    )

    print("✅ Datos normalizados y guardados.")
    return {
        "xx_train_file_path": xx_train_norm_path,
        "y_train_file_path": y_train_path,
        "xx_test_file_path": xx_test_norm_path,
        "y_test_file_path": y_test_path,
    }


def read_train_data(file_dict_ast):
    """
    Leemos los datos de entrenamiento
    """
    import ast  # noqa: PLC0415

    import pandas as pd  # noqa: PLC0415

    input_data = ast.literal_eval(file_dict_ast)
    xx_train_path = input_data["xx_train_file_path"]
    y_train_path = input_data["y_train_file_path"]

    xx_train = pd.read_csv(xx_train_path)
    y_train = pd.read_csv(y_train_path)
    print(f"📚 Datos de entrenamiento: X={xx_train.shape}, y={y_train.shape}")


def read_test_data(file_dict_ast):
    """
    Leemos los datos de testeo
    """
    import ast  # noqa: PLC0415

    import pandas as pd  # noqa: PLC0415

    input_data = ast.literal_eval(file_dict_ast)
    xx_test_path = input_data["xx_test_file_path"]
    y_test_path = input_data["y_test_file_path"]

    xx_test = pd.read_csv(xx_test_path)
    y_test = pd.read_csv(y_test_path)
    print(f"🧪 Datos de testeo: X={xx_test.shape}, y={y_test.shape}")


obtain_original_data_operator = PythonVirtualenvOperator(
    task_id="obtain_original_data",
    python_callable=obtain_original_data,
    requirements=["ucimlrepo"],
    system_site_packages=False,
    dag=dag,
)

make_dummies_variables_operator = PythonVirtualenvOperator(
    task_id="make_dummies_variables",
    python_callable=make_dummies_variables,
    requirements=["pandas"],
    op_args=["{{ ti.xcom_pull(task_ids='obtain_original_data') }}"],
    system_site_packages=False,
    dag=dag,
)

split_dataset_operator = PythonVirtualenvOperator(
    task_id="split_dataset",
    python_callable=split_dataset,
    requirements=["pandas", "scikit-learn"],
    op_args=["{{ ti.xcom_pull(task_ids='make_dummies_variables') }}"],
    system_site_packages=False,
    dag=dag,
)

normalize_data_operator = PythonVirtualenvOperator(
    task_id="normalize_data",
    python_callable=normalize_data,
    requirements=["pandas", "scikit-learn"],
    op_args=["{{ ti.xcom_pull(task_ids='split_dataset') }}"],
    system_site_packages=False,
    dag=dag,
)

read_train_data_operator = PythonVirtualenvOperator(
    task_id="read_train_data",
    python_callable=read_train_data,
    requirements=["pandas"],
    op_args=["{{ ti.xcom_pull(task_ids='normalize_data') }}"],
    system_site_packages=False,
    dag=dag,
)

read_test_data_operator = PythonVirtualenvOperator(
    task_id="read_test_data",
    python_callable=read_test_data,
    requirements=["pandas"],
    op_args=["{{ ti.xcom_pull(task_ids='normalize_data') }}"],
    system_site_packages=False,
    dag=dag,
)

(
    obtain_original_data_operator
    >> make_dummies_variables_operator
    >> split_dataset_operator
    >> normalize_data_operator
)
normalize_data_operator >> [read_train_data_operator, read_test_data_operator]
