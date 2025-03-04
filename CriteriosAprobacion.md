# Criterios de aprobación

## Objetivos de la materia:

El objetivo está centrado en disponibilizar las herramientas de machine learning en un entorno productivo, utilizando herramientas de MLOps.

## Evaluación

La evaluación de los conocimientos impartidos durante las clases será a modo de entrega de un trabajo práctico final. El trabajo es grupal (máximo 6 personas, mínimo 2 personas).

La idea de este trabajo es suponer que trabajamos para **ML Models and something more Inc.**, la cual ofrece un servicio que proporciona modelos mediante una REST API. Internamente, tanto para realizar tareas de DataOps como de MLOps, la empresa cuenta con Apache Airflow y MLflow. También dispone de un Data Lake en S3.

Ofrecemos dos tipos de evaluaciones:

 * **Nivel local** (nota entre 6 y 8): Implementar en local un ciclo de desarrollo del modelo que desarrollaron en Aprendizaje de Máquina hasta la generación final del artefacto del modelo entrenado. Deben usar un orquestador y buenas prácticas de desarrollo con buena documentación.
 * **Nivel en contenedores** (nota entre 8 y 10): Implementar el modelo que desarrollaron en Aprendizaje de Máquina en el ambiente productivo. Para ello, pueden usar los recursos que consideren apropiado. Los servicios disponibles de base son Apache Airflow, MLflow, PostgresSQL, MinIO, FastAPI. Todo está montado en Docker, por lo que además deben instalado Docker.

### Repositorio con el material

Las herramientas para poder armar el proyecto se encuentra en: 
[https://github.com/facundolucianna/amq2-service-ml](https://github.com/facundolucianna/amq2-service-ml).

Además, dejamos un ejemplo de aplicación en el branch [example_implementation](https://github.com/facundolucianna/amq2-service-ml/tree/example_implementation).

## Criterios de aprobación

Los criterios de aprobación son los siguientes:

1. El trabajo se entrega en dos partes. 
2. La entrega consiste en un repositorio en Github o Gitlab con la implementación y documentación. 
3. La fecha de entrega de la primera parte es en la clase 5 y la entrega final es 7 días después de la última clase.
4. El trabajo es obligatorio ser grupal para evaluar la dinámica de trabajo en un equipo de trabajo tipico.
5. La implementación debe de estar de acuerdo al nivel elegido. Sí es importante además de la implementación, hacer una buena documentación.
6. Son libres de incorporar o cambiar de tecnologías, pero es importante que lo implementado tenga un servicio de orquestación y algún servicio de ciclo de vida de modelos.   
7. La entrega es por medio del aula virtual de la asignatura y solo debe enviarse el link al repositorio en ambas entregas.
