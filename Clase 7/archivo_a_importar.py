
import sklearn
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeRegressor
import mlflow

model = DecisionTreeRegressor()
data = load_iris()

X = data.data
y = data.target

with mlflow.start_run():
    model.fit(X,y)
    mlflow.sklearn.log_model(model, "model")

