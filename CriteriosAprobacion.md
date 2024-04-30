# Criterios de aprobación

## Objetivos de la materia:

El objetivo está centrado en disponibilizar las herramientas de machine learning en un entorno productivo, utilizando herramientas de MLOPS.

## Evaluación

La evaluación de los conocimientos impartidos durante las clases será a modo de entrega de un trabajo práctico final. El trabajo es grupal (máximo 3 personas, mínimo 2 personas).

La idea de este trabajo es suponer que trabajamos para **ML Models and something more Inc.**, la cual ofrece un servicio que proporciona modelos mediante una REST API. Internamente, tanto para realizar tareas de DataOps como de MLOps, la empresa cuenta con Apache Airflow y MLflow. También dispone de un Data Lake en S3.

La tarea es implementar el modelo que desarrollaron en Aprendizaje de Máquina I en este ambiente productivo. Para ello, pueden usar los recursos que consideren apropiado. Los servicios disponibles de base son Apache Airflow, MLflow, PostgresSQL, MinIO, FastAPI. Todo está montado en Docker, por lo que además deben instalado Docker. 

### Repositorio con el material

Las herramientas para poder armar el proyecto se encuentra en: 
[https://github.com/facundolucianna/amq2-service-ml](https://github.com/facundolucianna/amq2-service-ml).

Recuerda que dejamos un ejemplo de aplicación en el branch [example_implementation](https://github.com/facundolucianna/amq2-service-ml/tree/example_implementation).

## Criterios de aprobación

Los criterios de aprobación son los siguientes:

1. La entrega consiste en un repositorio en Github o Gitlab con la implementación y documentación.
2. La fecha de entrega máxima es 7 días después de la última clase.
3. El trabajo es obligatorio ser grupal para evaluar la dinámica de trabajo en un equipo de trabajo tipico.
4. La implementación como minimo debe contener:
    - Un DAG en Apache Airflow. Puede ser cualquier tarea que se desee realizar, como entrenar el modelo, un proceso ETL, etc.
    - Un experimento en MLFlow de búsqueda de hiperparámetros.
    - Servir el modelo implementado en AMq1 en el servicio de RESTAPI.
    - Documentar (comentarios y docstring en scripts, notebooks, y asegurar que la documentación de FastAPI esté de acuerdo al modelo).
5. Son libres de incorporar o cambiar de tecnologías, pero es importante que lo implementado tenga un servicio de orquestación y algun servicio de ciclo de vida de modelos.   

## Link de formulario de Google para envio del trabajo (13Co2023)

El informe a entregar se debe envia mediante el siguiente formulario: [https://forms.gle/2H1JbQBdjj5FsFtX9](https://forms.gle/2H1JbQBdjj5FsFtX9). La fecha de entrega es el 28/04/2024 a las 23:59.
