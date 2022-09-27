# Databricks notebook source
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import mlflow
from sklearn.model_selection import train_test_split
import sklearn
from sklearn.tree import DecisionTreeClassifier

# COMMAND ----------

data = load_iris()

# COMMAND ----------

data.feature_names

# COMMAND ----------

X = data.data
y  = data.target

# COMMAND ----------

X

# COMMAND ----------

y

# COMMAND ----------

X_train, X_test, y_train, y_test = train_test_split(X, y)

# COMMAND ----------

model = DecisionTreeClassifier()

# COMMAND ----------

model.fit(X_train, y_train)

# COMMAND ----------

mlflow.start_run(experiment_id = "3829330798734503")

# COMMAND ----------

model.fit(X_train, y_train)

  
y_train_predicted = model.predict(X_train)
accuracy_train = (model.predict(X_train) == y_train).mean()
accuracy_test  = (model.predict(X_test)  == y_test).mean()

mlflow.log_metric("accuracy_train", accuracy_train)
mlflow.log_metric("accuracy_test", accuracy_test)

# COMMAND ----------

mlflow.sklearn.log_model(model, "model")

# COMMAND ----------

mlflow.set_tag("owner","Camilo")
mlflow.set_tag("periodo","Clase 4 ml2")

# COMMAND ----------

mlflow.end_run()

# COMMAND ----------

experiment_id = "2446110300768704"


mlflow.autolog()
with mlflow.start_run(experiment_id = experiment_id):
  model.fit(X_train, y_train)
  mlflow.sklearn.log_model(model, "model")
  
  y_train_predicted = model.predict(X_train)
  accuracy_train = (model.predict(X_train) == y_train).mean()
  accuracy_test  = (model.predict(X_test)  == y_test).mean()
  
  
#   mlflow.log_metric("accuracy_train", accuracy_train)
#   mlflow.log_metric("accuracy_test", accuracy_test)
  
  mlflow.set_tag("owner","Camilo")