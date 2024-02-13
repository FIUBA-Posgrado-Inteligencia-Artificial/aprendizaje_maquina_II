from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'alex_barria_c',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'databricks_job_trigger',
    default_args=default_args,
    description='A DAG to trigger a Databricks job',
    schedule_interval='@daily',
    catchup=False,
)

# Databricks cluster config
num_workers = 0
driver_node_type_id = "Standard_DS3_v2"
node_type_id = "Standard_F4"
spark_version = "13.3.x-scala2.12"

cluster = {
    "spark_version": spark_version,
    "num_workers": num_workers,
    "driver_node_type_id": driver_node_type_id,
    "node_type_id": node_type_id,
}

params = {
    'new_cluster': cluster,
    'notebook_task': {
        'notebook_path': '/Users/alexbarria_14@hotmail.com/clase_7/main_task'
    }
}

libraries_list = []

## Example of libraries_list
# libraries_list = [
#                   {'pypi': {'package': 'mlflow==2.7.1'}},
#                   {'pypi': {'package': 'scikit-learn==1.1.1'}},
# ]

databricks_operator = DatabricksSubmitRunOperator(
    dag=dag,
    do_xcom_push=True,
    databricks_conn_id='databricks-ab',  # Use the Conn Id specified in the connection UI
    task_id='run_databricks_job',
    libraries=libraries_list,
    json=params,
    timeout_seconds=600,
)