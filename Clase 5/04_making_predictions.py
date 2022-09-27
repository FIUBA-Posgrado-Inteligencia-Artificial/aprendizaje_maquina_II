# Databricks notebook source
import pandas as pd
import sklearn
import mlflow
import pandas as pd

# COMMAND ----------

df = spark.sql("select * from opts_tools_ds.apu_delete_after_use_2")
df = df.toPandas()
df

# COMMAND ----------

data = df.drop("fecha", axis = 1)
fecha = df["fecha"]
data

# COMMAND ----------

logged_model = 'runs:/5683bbfa87d44e52a16d8ac23e1b2573/model'
loaded_model = mlflow.sklearn.load_model(logged_model)

df["target"] = loaded_model.predict(data)
df

# COMMAND ----------

data_spark = spark.createDataFrame(df)
data_spark

# COMMAND ----------

data_spark.createTempView("ml2")

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select * 
# MAGIC from ml2

# COMMAND ----------

data_spark = spark.createDataFrame(df)
data_spark.createOrReplaceTempView("ml2")

# COMMAND ----------

# MAGIC %sql 
# MAGIC 
# MAGIC insert into opts_tools_ds.apu_model_results  (select sepal_length, sepal_width, petal_length, petal_width, target,fecha from ml2)

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select count(*) from opts_tools_ds.apu_model_results

# COMMAND ----------

