import random
import fastapi
from pydantic import BaseModel, Field

app = fastapi.FastAPI()


class InputFeatures(BaseModel):
    size: float = Field(
        description="Size of the animal in cm",
        ge=0,
        le=200,
    )
    height: float = Field(
        description="Height of the animal in cm",
        ge=0,
        le=200,
    )
    weight: float = Field(
        description="Weight of the animal in Kg",
        ge=0,
        le=150,
    )
    number_of_whiskers: int = Field(
        description="Number of whiskers in the animal snout",
        ge=0,
        le=50,
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "size": 25,
                    "height": 30.3,
                    "weight": 8,
                    "number_of_whiskers": 12,
                }
            ]
        }
    }


class OutputPrediction(BaseModel):
    prediction: str = Field(
        description="Output of the model.",
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "prediction": "Cat",
                }
            ]
        }
    }


class MLModel:
    @staticmethod
    def predict(size, height, weight, number_of_whiskers):
        value = random.randint(0, 1)
        output = "Dog"
        if value == 0:
            output = "Cat"
        # Placeholder prediction logic
        return OutputPrediction(prediction=output)


class APIInfo(BaseModel):
    name: str = "ML Model API"
    description: str = "A simple machine learning model API for predicting cats or dogs."
    version: str = "1.0"


# Create an instance of the placeholder model
ml_model = MLModel()


# Endpoint to get API information
@app.get("/", response_model=APIInfo)
async def get_api_info() -> APIInfo:
    return APIInfo()


# Endpoint to make predictions
@app.post("/predict/")
async def predict(features: InputFeatures) -> OutputPrediction:
    prediction = ml_model.predict(features.size, features.height, features.weight, features.number_of_whiskers)
    return prediction
