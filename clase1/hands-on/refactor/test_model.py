import pickle

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import RocCurveDisplay, f1_score


def load_datasets(path_x_test: str, path_y_test: str) -> tuple:
    """
    Carga el dataset de testeo, tanto las entradas como las salidas

    :param path_x_test: String con el path del csv con las entradas de testeo
    :type path_x_test: str
    :param path_y_test: String con el path del csv con la salida de testeo
    :type path_y_test: str
    :returns: Tupla con las entradas y salida de testeo
    :rtype: tuple
    """

    xx_test = np.loadtxt(path_x_test, delimiter=",", dtype=float)
    y_test = np.loadtxt(path_y_test, delimiter=",", dtype=float, skiprows=1, usecols=1)

    return xx_test, y_test


def load_model_binary(path_model: str):
    """
    Carga el artefacto del modelo

    :param path_model: Ubicación para leer el artefacto del modelo
    :type path_model: str
    :returns: Modelo binario
    :rtype: sklearn model
    """

    return pickle.load(open(path_model, "rb"))


def test_model_f1(model, xx_test, y_test):
    """
    Testea el modelo mediante la metrica F1

    :param model: Modelo de machine learning
    :type model: sklearn model
    :param xx_test: Array de numpy con las entradas de testeo
    :type xx_test: np.ndarray
    :param y_test: Array de numpy con la salida de testeo
    :type y_test: np.ndarray
    """

    y_pred = model.predict(xx_test)
    f1 = f1_score(y_test, y_pred)

    # Generamos artefacto
    with open("./log_testing_metric.txt", "w") as f:
        f.write("F1-Score: ")
        f.write(f"{f1}\n")


def obtain_roc_curve(model, xx_test, y_test):
    """
    Genera el gráfico de curva ROC para el modelo dado
    el conjunto de testeo

    :param model: Modelo de machine learning
    :type model: sklearn model
    :param xx_test: Array de numpy con las entradas de testeo
    :type xx_test: np.ndarray
    :param y_test: Array de numpy con la salida de testeo
    :type y_test: np.ndarray
    """

    _, ax = plt.subplots(figsize=(5, 5))
    RocCurveDisplay.from_estimator(model, xx_test, y_test, ax=ax)
    plt.savefig("roc.png", bbox_inches="tight")


# Testeamos el modelo
X_test, y_test = load_datasets("./X_test_scaled.csv", "./y_test.csv")
model = load_model_binary("./best_model.pkl")
test_model_f1(model, X_test, y_test)
obtain_roc_curve(model, X_test, y_test)
