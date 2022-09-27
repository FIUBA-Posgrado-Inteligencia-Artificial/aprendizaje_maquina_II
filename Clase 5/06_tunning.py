# Databricks notebook source
import mlflow

# COMMAND ----------

mlflow.set_tag

# COMMAND ----------

for run1 in [1,2]:
  with mlflow.start_run():
    for run2 in ["a","b"]:
      with mlflow.start_run(nested = True):
        mlflow.set_tag("run1",run1)
        mlflow.set_tag("run2",run2)