# Criterios de aprobación

## Objetivos de la materia:

El objetivo está centrado en disponibilizar las herramientas de machine learning en un entorno productivo, utilizando herramientas de MLOPS.

## Evaluación

La evaluación de los conocimientos impartidos durante las clases será a modo de entrega de un trabajo práctico final. El trabajo puede ser individual o grupal (máximo 4 personas).

La idea de este trabajo es suponer que trabajamos para **ML Models and something more Inc.**, la cual ofrece un servicio que proporciona modelos mediante una REST API. Internamente, tanto para realizar tareas de DataOps como de MLOps, la empresa cuenta con Apache Airflow y MLflow. También dispone de un Data Lake en S3.

La tarea es implementar el modelo que desarrollaron en Aprendizaje de Máquina I en este ambiente productivo. Para ello, pueden usar los recursos que consideren apropiado. Los servicios disponibles de base son Apache Airflow, MLflow, PostgresSQL, MinIO, FastAPI. Todo está montado en Docker, por lo que además deben instalado Docker. 

## Criterios de aprobación

Los criterios de aprobación son los siguientes:

1. La entrega consiste en un repositorio en Github o Gitlab con la implementación y documentación.
2. La fecha de entrega máxima es 7 días después de la última clase.
3. La implementación como minimo debe contener:
    - Un DAG en Apache Airflow. Puede ser cualquier tarea que se desee realizar, como entrenar el modelo, un proceso ETL, etc.
    - Un experimento en MLflow de búsqueda de hiperparámetros.
    - Servir el modelo implementado en AMq1 en el servicio de RESTAPI.
    - Documentar (comentarios y docstring en scripts, notebooks, y asegurar que la documentación de FastAPI esté de acuerdo al modelo).
4. Son libres de incorporar o cambiar de tecnologias, pero es importante que lo implementado tenga un servicion de orquestación y algun servicio de ciclo de vida de modelos.   

## Link de formulario de Google para envio del trabajo (13Co2023)

El informe a entregar se debe envia mediante el siguiente formulario: [Proximamente](Proximamente). La fecha de entrega es el XX/XX/2024 a las XX:XX.
