import pickle
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import f1_score, RocCurveDisplay


def load_datasets(path_X_test: str, path_y_test: str) -> tuple:
    """
    Carga el dataset de testeo, tanto las entradas como las salidas

    :param path_X_test: String con el path del csv con las entradas de testeo
    :type path_X_test: str
    :param path_y_test: String con el path del csv con la salida de testeo
    :type path_y_test: str
    :returns: Tupla con las entradas y salida de testeo
    :rtype: tuple
    """

    X_test = np.loadtxt(path_X_test, delimiter=",", dtype=float)
    y_test = np.loadtxt(path_y_test, delimiter=",", dtype=float,
                        skiprows=1, usecols=1)

    return X_test, y_test


def load_model_binary(path_model: str):
    """
    Carga el artefacto del modelo

    :param path_model: Ubicación para leer el artefacto del modelo
    :type path_model: str
    :returns: Modelo binario
    :rtype: sklearn model
    """

    return pickle.load(open(path_model, 'rb'))


def test_model_f1(model, X_test, y_test):
    """
    Testea el modelo mediante la metrica F1

    :param model: Modelo de machine learning
    :type model: sklearn model
    :param X_test: Array de numpy con las entradas de testeo
    :type X_test: np.array
    :param y_test: Array de numpy con la salida de testeo
    :type y_test: np.array
    """

    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred)

    # Generamos artefacto
    with open("./log_testing_metric.txt", "w") as f:
        f.write("F1-Score: ")
        f.write('%s\n' % f1)


def obtain_ROC_curve(model, X_test, y_test):
    """
    Genera el gráfico de curva ROC para el modelo dado
    el conjunto de testeo

    :param model: Modelo de machine learning
    :type model: sklearn model
    :param X_test: Array de numpy con las entradas de testeo
    :type X_test: np.array
    :param y_test: Array de numpy con la salida de testeo
    :type y_test: np.array
    """

    _, ax = plt.subplots(figsize=(5, 5))
    RocCurveDisplay.from_estimator(model, X_test, y_test, ax=ax)
    plt.savefig('roc.png', bbox_inches='tight')


# Testeamos el modelo
X_test, y_test = load_datasets("./X_test_scaled.csv", "./y_test.csv")
model = load_model_binary("./best_model.pkl")
test_model_f1(model, X_test, y_test)
obtain_ROC_curve(model, X_test, y_test)
