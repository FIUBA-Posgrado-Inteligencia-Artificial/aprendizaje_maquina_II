import random
import fastapi

app = fastapi.FastAPI()


class MLModel:
    @staticmethod
    def predict(size, height, weight, number_of_whiskers):
        value = random.randint(0, 1)
        output = "Dog"
        if value == 0:
            output = "Cat"
        # Placeholder prediction logic
        return {"prediction": output}


# Create an instance of the placeholder model
ml_model = MLModel()

# Endpoint to make predictions
@app.post("/predict/")
async def predict(size: float, height: float, weight: float, number_of_whiskers: int):
    prediction = ml_model.predict(size, height, weight, number_of_whiskers)
    return prediction
