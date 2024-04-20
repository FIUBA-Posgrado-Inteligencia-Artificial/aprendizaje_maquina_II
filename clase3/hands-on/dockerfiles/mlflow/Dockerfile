FROM python:3.11-slim

COPY requirements.txt /requirements.txt
RUN apt-get update && apt-get install -y wget
RUN pip install --upgrade pip
RUN pip install mlflow[extras] psycopg2-binary boto3 cryptography pymysql
RUN pip install --no-cache-dir -r /requirements.txt

EXPOSE 5000