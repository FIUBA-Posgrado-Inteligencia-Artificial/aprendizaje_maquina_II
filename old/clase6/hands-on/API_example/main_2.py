import random
import fastapi
from pydantic import BaseModel

app = fastapi.FastAPI()


class InputFeatures(BaseModel):
    size: float
    height: float
    weight: float
    number_of_whiskers: int


class OutputPrediction(BaseModel):
    prediction: str


class MLModel:
    @staticmethod
    def predict(size, height, weight, number_of_whiskers):
        value = random.randint(0, 1)
        output = "Dog"
        if value == 0:
            output = "Cat"
        # Placeholder prediction logic
        return OutputPrediction(prediction=output)


# Create an instance of the placeholder model
ml_model = MLModel()

# Endpoint to make predictions
@app.post("/predict/")
async def predict(features: InputFeatures) -> OutputPrediction:
    prediction = ml_model.predict(features.size, features.height, features.weight, features.number_of_whiskers)
    return prediction
