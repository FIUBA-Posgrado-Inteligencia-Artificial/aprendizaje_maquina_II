FROM python:3.12-slim

COPY requirements.txt /requirements.txt
RUN apt-get update && apt-get install -y wget
RUN pip install --upgrade pip
RUN pip install mlflow[extras]
RUN pip install --no-cache-dir -r /requirements.txt

EXPOSE 5000