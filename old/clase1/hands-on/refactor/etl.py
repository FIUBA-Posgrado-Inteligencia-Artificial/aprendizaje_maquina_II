import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_data_from_source(path: str,
                          filename: str) -> pd.DataFrame:
    """
    Carga los datos crudos

    :param path: Path donde está ubicado el archivo CSV con los datos crudos
    :type path: str
    :param filename: Nombre del archivo CSV
    :type filename: str
    :returns: Los datos crudos como un archivo CSV
    :rtype: pd.DataFrame
    """

    # Cargamos el dataset
    return pd.read_csv(path + filename)


def make_dummies_variables(dataset: pd.DataFrame,
                           categories_list: list) -> pd.DataFrame:
    """
    Convierte a las variables categóricas en one-hot-encoding

    :param dataset: Dataframe con el dataset
    :type dataset: pd.DataFrame
    :param categories_list: Lista con el nombre de las columnas categóricas
    :type categories_list: list
    :returns: Dataset con las columnas convertidas
    :rtype: pd.DataFrame
    """

    dataset_with_dummies = pd.get_dummies(data=dataset,
                                          columns=categories_list,
                                          drop_first=True)

    # Generamos un artefacto
    with open("./log_columns_dummies.txt", "w") as f:
        f.write("New columns after dummies:\n")
        for category in dataset_with_dummies.columns:
            f.write('%s\n' % category)

    return dataset_with_dummies


def split_dataset(dataset: pd.DataFrame, test_size: float,
                  target_column: str, is_stratified: bool) -> tuple:
    """
    Genera una división del dataset en una parte de entrenamiento y otra de validación

    :param dataset: Dataframe con el dataset
    :type dataset: pd.DataFrame
    :param test_size: Proporción del set de testeo
    :type test_size: float
    :param target_column: Nombre de la columna de target para el entrenamiento
    :type target_column: str
    :param is_stratified: Si es True, se separa el dataset respetando la proporción del target
    :type is_stratified: bool
    :returns: Tupla con las entradas y salidas de entrenamiento y testeo.
    :rtype: tuple
    """

    X = dataset.drop(columns=target_column)
    y = dataset[[target_column]]

    if is_stratified:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, stratify=y)
    else:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, stratify=y)

    # Generamos artefactos
    X_train.to_csv("./X_train.csv")
    X_test.to_csv("./X_test.csv")
    y_train.to_csv("./y_train.csv")
    y_test.to_csv("./y_test.csv")

    return X_train, X_test, y_train, y_test


def standardize_inputs(X_train: pd.DataFrame,
                      X_test: pd.DataFrame) -> tuple:
    """
    Estandarizador de las columnas numéricas

    :param X_train: Dataframe con el dataset de entradas de entrenamiento
    :type X_train: pd.DataFrame
    :param X_test: Dataframe con el dataset de entradas de testeo
    :type X_test: pd.DataFrame
    :returns: Tupla con las entradas de entrenamiento y testeo normalizadas.
    :rtype: tuple
    """

    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)

    # Generamos artefactos
    np.savetxt("./X_train_scaled.csv", X_train, delimiter=",")
    np.savetxt("./X_test_scaled.csv", X_test, delimiter=",")


# Proceso de Extract, Load and Transform
dataset = load_data_from_source("./", "heart.csv")
dataset = make_dummies_variables(dataset,
                                 ["cp", "restecg", "slope", "ca", "thal"])
X_train, X_test, y_train, y_test = split_dataset(dataset, 0.3, 'target', True)
standardize_inputs(X_train, X_test)
