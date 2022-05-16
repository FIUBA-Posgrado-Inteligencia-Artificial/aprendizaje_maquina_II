# Databricks notebook source
import mlflow
import pandas as pd

# COMMAND ----------

#logged_model = 'runs:/fbbce7ce8e744d45ac33253157adb616/model'

logged_model = "runs:/14073543e66b472796c2f89ed1c68e0c/model"
loaded_model = mlflow.sklearn.load_model(logged_model)

# COMMAND ----------

loaded_model.predict(data)

# COMMAND ----------

data = load_iris().data

# COMMAND ----------

data

# COMMAND ----------



# COMMAND ----------

from sklearn.datasets import load_iris

# COMMAND ----------

logged_model = 'runs:/5b98874e00a84fca9b9326e0d4147c88/model'
loaded_model = mlflow.sklearn.load_model(logged_model)

# Predict on a Pandas DataFrame.

loaded_model.predict(pd.DataFrame(data))