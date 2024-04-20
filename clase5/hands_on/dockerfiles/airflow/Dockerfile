FROM apache/airflow:2.8.1
COPY requirements.txt /requirements.txt

RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user apache-airflow[virtualenv]==2.8.1 -r /requirements.txt
