# Criterios de aprobación

## Objetivos de la materia:

El objetivo está centrado en disponibilizar las herramientas de machine learning en un entorno productivo, utilizando herramientas de MLOPS.

## Evaluación

La evaluación de los conocimientos impartidos durante las clases será a modo de entrega de un trabajo práctico final. El trabajo es grupal (máximo 6 personas, mínimo 2 personas).

La idea de este trabajo es suponer que trabajamos para **ML Models and something more Inc.**, la cual ofrece un servicio que proporciona modelos mediante una REST API. Internamente, tanto para realizar tareas de DataOps como de MLOps, la empresa cuenta con Apache Airflow y MLflow. También dispone de un Data Lake en S3.

Ofrecemos tres tipos de evaluaciones:

 * **Nivel fácil** (nota entre 4 y 5): Hacer funcionar el ejemplo de aplicación [example_implementation](https://github.com/facundolucianna/amq2-service-ml/tree/example_implementation). Filmar un video del sistema funcionando:
   * Ejecutar en Airflow el DAG llamado `process_etl_heart_data`
   * Ejecuta la notebook (ubicada en `notebook_example`) para realizar la búsqueda de hiperparámetros y entrenar el mejor modelo.
   * Utilizar la REST-API del modelo.
   * Ejecutar en Airflow el DAG llamado `process_etl_heart_data` y luego `retrain_the_model`.
   * En todos estos pasos verificar lo que muestra MLFlow.
 * **Nivel medio** (nota entre 6 y 8): Implementar en local usando Metaflow el ciclo de desarrollo del modelo que desarrollaron en Aprendizaje de Máquina I y generar un archivo para predicción en bache (un csv o un archivo de SQLite). Sería implementar algo parecido a [batch_example](https://github.com/facundolucianna/amq2-service-ml/tree/batch_example), pero sin la parte del servicio de Docker. La nota puede llegar a 10 si implementan una base de datos (ya sea KVS u otro tipo) con los datos de la predicción en bache.
 * **Nivel alto** (nota entre 8 y 10): Implementar el modelo que desarrollaron en Aprendizaje de Máquina I en este ambiente productivo. Para ello, pueden usar los recursos que consideren apropiado. Los servicios disponibles de base son Apache Airflow, MLflow, PostgresSQL, MinIO, FastAPI. Todo está montado en Docker, por lo que además deben instalado Docker. 

### Repositorio con el material

Las herramientas para poder armar el proyecto se encuentra en: 
[https://github.com/facundolucianna/amq2-service-ml](https://github.com/facundolucianna/amq2-service-ml).

Además dejamos un ejemplo de aplicación en el branch [example_implementation](https://github.com/facundolucianna/amq2-service-ml/tree/example_implementation).

## Criterios de aprobación

Los criterios de aprobación son los siguientes:

1. La entrega consiste en un repositorio en Github o Gitlab con la implementación y documentación. Salvo el nivel fácil que es un link al video.
2. La fecha de entrega máxima es 7 días después de la última clase.
3. El trabajo es obligatorio ser grupal para evaluar la dinámica de trabajo en un equipo de trabajo tipico.
4. La implementación debe de estar de acuerdo al nivel elegido. Si es importante además de la implementación, hacer una buena documentación.
5. Son libres de incorporar o cambiar de tecnologías, pero es importante que lo implementado tenga un servicio de orquestación y algun servicio de ciclo de vida de modelos.   

## Link de formulario de Google para envio del trabajo (14Co2023)

El informe a entregar se debe envia mediante el siguiente formulario: [https://forms.gle/2H1JbQBdjj5FsFtX9](https://forms.gle/2H1JbQBdjj5FsFtX9). La fecha de entrega es el 28/04/2024 a las 23:59.
