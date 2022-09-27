# Databricks notebook source
# MAGIC %sql 
# MAGIC 
# MAGIC create table if not exists opts_tools_ds.apu_delete_after_use_2
# MAGIC (
# MAGIC sepal_length double,
# MAGIC sepal_width double,
# MAGIC petal_length double,
# MAGIC petal_width double,
# MAGIC fecha string 
# MAGIC )
# MAGIC 
# MAGIC USING parquet
# MAGIC location 's3a://mediation-bucket-prod/gold/waterfall_opt_sm/apu_delete_after_use_2'

# COMMAND ----------

# MAGIC %sql 
# MAGIC 
# MAGIC select *
# MAGIC from opts_tools_ds.apu_delete_after_use_2

# COMMAND ----------

df = spark.sql("select * from opts_tools_ds.apu_delete_after_use_2")

df = df.toPandas()
df

# COMMAND ----------

# MAGIC %sql 
# MAGIC 
# MAGIC create table if not exists opts_tools_ds.apu_model_results
# MAGIC (
# MAGIC sepal_length double,
# MAGIC sepal_width double,
# MAGIC petal_length double,
# MAGIC petal_width double,
# MAGIC target int,
# MAGIC fecha string 
# MAGIC )
# MAGIC 
# MAGIC USING parquet
# MAGIC location 's3a://mediation-bucket-prod/gold/waterfall_opt_sm/apu_model_results'

# COMMAND ----------

