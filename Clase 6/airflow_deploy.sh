mkdir -p airflow
export AIRFLOW_HOME=$(pwd)/airflow
echo $AIRFLOW_HOME
airflow standalone
