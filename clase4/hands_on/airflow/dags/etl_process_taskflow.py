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
    tags=["ETL", "TaskFlow"],
    default_args=default_args,
    catchup=False,
)
def process_etl_taskflow():

    @task.virtualenv(
        task_id="obtain_original_data",
        requirements=["ucimlrepo~=0.0",
                      "pandas~=2.0"],
    )
    def get_data():
        """
        Carga los datos desde de la fuente
        """
        from ucimlrepo import fetch_ucirepo

        # Obtenemos el dataset
        heart_disease = fetch_ucirepo(id=45)

        dataframe = heart_disease.data.original

        # Todos valores mayores a cero es una enfermedad cardiaca
        dataframe.loc[dataframe["num"] > 0, "num"] = 1

        path = "./data.csv"
        dataframe.to_csv("./data.csv", index=False)

        # Enviamos un mensaje para el siguiente nodo
        return path

    @task(
        task_id="make_dummies_variables",
        multiple_outputs=True
    )
    def make_dummies_variables(path_input):
        """
        Convierte a las variables en Dummies
        """
        import pandas as pd

        a = 0
        b = 0

        if path_input:

            dataset = pd.read_csv(path_input)

            # Limpiamos duplicados
            dataset.drop_duplicates(inplace=True, ignore_index=True)
            # Y quitamos nulos
            dataset.dropna(inplace=True, ignore_index=True)

            # Forzamos las categorias en las columnas
            dataset["cp"] = dataset["cp"].astype(int)
            dataset["restecg"] = dataset["restecg"].astype(int)
            dataset["slope"] = dataset["slope"].astype(int)
            dataset["ca"] = dataset["ca"].astype(int)
            dataset["thal"] = dataset["thal"].astype(int)

            categories_list = ["cp", "restecg", "slope", "ca", "thal"]
            dataset_with_dummies = pd.get_dummies(data=dataset,
                                                  columns=categories_list,
                                                  drop_first=True)
            dataset_with_dummies.to_csv("./data_clean_dummies.csv", index=False)

            # Enviamos dos mensajes entre nodo
            # OBS: Recordad que no se mandan mucha información, solo mensajes de comunicación. Si querés pasar dataset
            # entre nodos, es mejor guardar en algún lado y pasar el path o similar.
            a = dataset_with_dummies.shape[0]
            b = dataset_with_dummies.shape[1]

        return {"observations": a, "columns": b}

    @task.virtualenv(
        task_id="split_dataset",
        requirements=["pandas~=1.5",
                      "scikit-learn==1.3.2"],
    )
    def split_dataset(obs, col):
        """
        Genera el dataset y obtiene set de testeo y evaluación
        """
        import pandas as pd
        from sklearn.model_selection import train_test_split

        dataset = pd.read_csv("./data_clean_dummies.csv")

        # Leemos el mensaje del DAG anterior
        if dataset.shape[0] == obs and dataset.shape[1] == col:
            X = dataset.drop(columns="num")
            y = dataset[["num"]]

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

            X_train.to_csv("./X_train.csv", index=False)
            X_test.to_csv("./X_test.csv", index=False)
            y_train.to_csv("./y_train.csv", index=False)
            y_test.to_csv("./y_test.csv", index=False)


    @task.virtualenv(
        task_id="normalize_numerical_features",
        requirements=["pandas~=2.0",
                      "scikit-learn==1.3.2"]
    )
    def normalize_data():
        """
        Estandarizamos los datos
        """
        import pandas as pd
        from sklearn.preprocessing import StandardScaler

        X_train = pd.read_csv("./X_train.csv")
        X_test = pd.read_csv("./X_test.csv")

        sc_X = StandardScaler(with_mean=True, with_std=True)
        X_train_arr = sc_X.fit_transform(X_train)
        X_test_arr = sc_X.transform(X_test)

        X_train = pd.DataFrame(X_train_arr, columns=X_train.columns)
        X_test = pd.DataFrame(X_test_arr, columns=X_test.columns)

        X_train.to_csv("./X_train.csv", index=False)
        X_test.to_csv("./X_test.csv", index=False)

    @task.virtualenv(
        task_id="read_train_data",
        requirements=["pandas~=2.0",
                      "scikit-learn==1.3.2"]
    )
    def read_train_data():
        """
        Leemos los datos de entrenamiento
        """
        import pandas as pd

        X_train = pd.read_csv("./X_train.csv")
        y_train = pd.read_csv("./y_train.csv")

        print(f"Las X de entrenamiento son {X_train.shape} y las y son {y_train.shape}")

    @task.virtualenv(
        task_id="read_test_data",
        requirements=["pandas~=2.0",
                      "scikit-learn==1.3.2"]
    )
    def read_test_data():
        """
        Leemos los datos de testeo
        """
        import pandas as pd

        X_test = pd.read_csv("./X_test.csv")
        y_test = pd.read_csv("./y_test.csv")

        print(f"Las X de testeo son {X_test.shape} y las y son {y_test.shape}")

    path_input = get_data()
    dummies_output = make_dummies_variables(path_input)
    split_dataset(dummies_output["observations"], dummies_output["columns"]) >> normalize_data() >> [read_train_data(),
                                                                                                     read_test_data()]

dag = process_etl_taskflow()
