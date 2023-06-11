"""
Model.py

En este script se definen las funciones necesarias para entrenar un modelo RandomForest Classifier
sobre el conjunto de datos de Iris.
"""

import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from pydantic import BaseModel
import joblib


class IrisSpecies(BaseModel):
    """
    Clase que describe el tipo de dato para cada predicción
    """
    sepal_length: float 
    sepal_width: float 
    petal_length: float 
    petal_width: float


class IrisModel:
    """
    Clase para entrenar el modelo y efectuar predicciones
    """
    def __init__(self):
        """
        Constructor de la clase. Carga el dataset y el modelo en caso de que exista.
        Si el modelo no existe, el método _train_model es llamado y  guarda un modelo
        """
        self.df = pd.read_csv('iris.csv')
        self.model_fname_ = 'iris_model.pkl'
        try:
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            self.model = self._train_model()
            joblib.dump(self.model, self.model_fname_)

    def _train_model(self):
        """
        Método para entrenar el modelo utilizando RandomForest classifier
        """
        X = self.df.drop('species', axis=1)
        y = self.df['species']
        rfc = RandomForestClassifier()
        model = rfc.fit(X, y)
        return model

    def predict_species(self, sepal_length, sepal_width, petal_length, petal_width):
        """
        Método para realizar predicciones basadas en los datos brindados por el usuario.
        Retorna la especie predicha con su probabilidad.
        """
        data_in = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = self.model.predict(data_in)
        probability = self.model.predict_proba(data_in).max()
        return prediction[0], probability
    
    # Método para implementar gradio
    def predict_species_to_gradio(self, sepal_length, sepal_width, petal_length, petal_width):
        """
        Método para realizar predicciones basadas en los datos brindados por el usuario.
        Retorna la especie predicha con su probabilidad en formato diccionario.
        """
        data_in = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = self.model.predict(data_in)
        probability = self.model.predict_proba(data_in).max()
        return {prediction[0]: probability}
