import pickle

import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC


def load_datasets(path_x_train: str, path_y_train: str) -> tuple:
    """
    Carga el dataset de entrenamiento, tanto las entradas como las salidas

    :param path_x_train: String con el path del csv con las entradas de entrenamiento
    :type path_x_train: str
    :param path_y_train: String con el path del csv con la salida de entrenamiento
    :type path_y_train: str
    :returns: Tupla con las entradas y salida de entrenamiento
    :rtype: tuple
    """

    xx_train = np.loadtxt(path_x_train, delimiter=",", dtype=float)
    y_train = np.loadtxt(
        path_y_train, delimiter=",", dtype=float, skiprows=1, usecols=1
    )

    return xx_train, y_train


def grid_search_best_params(
    xx_train: np.ndarray, y_train: np.ndarray, path_best_model: str
):
    """
    Realiza una búsqueda de grilla de los mejores hiper-parámetros para un SVC
    dado el dataset de entrenamiento. Se elige el mejor modelo y se guarda el binario.

    :param xx_train: Array de numpy con las entradas de entrenamiento
    :type xx_train: np.ndarray
    :param y_train: Array de numpy con la salida de entrenamiento
    :type y_train: np.ndarray
    :param path_best_model: Ubicación a guardar el artefacto del modelo
    :type path_best_model: str
    """

    svm = SVC()

    grid = GridSearchCV(
        svm,
        [
            {
                "C": [0.01, 0.1, 1, 5, 10, 100],
                "gamma": [0.1, 0.5, 1, 2, 10, 100],
                "kernel": ["rbf"],
            },
            {
                "C": [0.01, 0.1, 1, 5, 10, 100],
                "degree": [2, 3, 4, 5, 6],
                "kernel": ["poly"],
            },
        ],
        refit=True,
        cv=5,
        scoring="f1",
    )

    grid.fit(X_train, y_train)

    with open("./log_training.txt", "w") as f:
        f.write("Best model parameters:\n")
        f.write(f"{grid.best_params_}\n")
        f.write(f"Type: {grid.scorer_} - Score: {grid.best_score_}\n")

    # Generamos el artefacto del modelo en binario
    pickle.dump(grid.best_estimator_, open(path_best_model, "wb"))


# Entrenamos el modelo
X_train, y_train = load_datasets("./X_train_scaled.csv", "./y_train.csv")
grid_search_best_params(X_train, y_train, "./best_model.pkl")
