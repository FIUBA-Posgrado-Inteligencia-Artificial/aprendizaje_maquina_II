# Databricks notebook source
import mlflow

# COMMAND ----------

model_name = "uba_ml2"

result = mlflow.register_model("runs:/14073543e66b472796c2f89ed1c68e0c/model",model_name)
# result = mlflow.register_model("runs:/5683bbfa87d44e52a16d8ac23e1b2573/model",model_name)

# COMMAND ----------


model = mlflow.sklearn.load_model(
    model_uri=f"models:/uba_ml2/2"
)

# COMMAND ----------

model

# COMMAND ----------

stage = "Production"
# stage = "Staging"
#stage = "None"

model = mlflow.sklearn.load_model(
    model_uri=f"models:/uba_ml2/{stage}"
)

# COMMAND ----------

model

# COMMAND ----------

model

# COMMAND ----------

model