# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Model import IrisModel, IrisSpecies


# Creación de la app y el objeto modelo
app = FastAPI()
model = IrisModel()

# Exponer la funcionalidad de predicción, utilizar el JSON para hacer predicciones
@app.post('/predict')
def predict_species(iris: IrisSpecies):
    data = iris.dict()
    prediction, probability = model.predict_species(
        data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']
    )
    return {
        'prediction': prediction,
        'probability': probability
    }

# Correr la API con uvicorn en http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)