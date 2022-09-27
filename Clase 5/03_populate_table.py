# Databricks notebook source
# MAGIC %sql
# MAGIC 
# MAGIC select count(*) from opts_tools_ds.apu_delete_after_use_2

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC insert into opts_tools_ds.apu_delete_after_use_2 values (0., 0. , 0., 0., "2022-01-03")

# COMMAND ----------

spark.sql("insert into opts_tools_ds.apu_delete_after_use_2 values (0., 0. , 0., 0., 'apu')")

# COMMAND ----------

