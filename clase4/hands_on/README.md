# Hands-on - Usando Apache Airflow para Sincronización de Tareas

En el mundo del flujo de trabajo y la sincronización de tareas, Apache Airflow es una herramienta ampliamente 
utilizada. Más allá de la simple ejecución de tareas, Airflow permite la creación, planificación y monitoreo de flujos 
de trabajo complejos.

En este hands-on, exploraremos cómo utilizar Apache Airflow para la sincronización de tareas en el contexto de 
procesos de datos. Vamos a crear un DAG de un proceso ETL, explorando tanto la implementación con TaskFlow como la
definición de DAGs de manera más tradicional.

Vamos a dividir este *hands-on* en dos formas de ejecutar MLFlow:

- Usando Apache Airflow para Sincronización de Tareas mediante servicio modo local — carpeta `local_version`
- Usando Apache Airflow para Sincronización de Tareas mediante servicio dockerizado — carpeta `container_version`

Ambas formas son muy similares en funcionalidad, pero difieren en la forma en que se instalan y gestionan los servicios:

- La versión local es ideal para entornos de desarrollo o pruebas individuales, donde se desea ejecutar Airflow directamente en un entorno virtual o en el sistema del usuario. Es simple de configurar, rápida para comenzar y útil para comprender los conceptos básicos sin depender de contenedores ni redes.

- La versión dockerizada encapsula toda la infraestructura de Airflow (scheduler, webserver, worker, base de datos, etc.) dentro de contenedores Docker, permitiendo una ejecución más cercana a un entorno de producción. Esto facilita la portabilidad, el aislamiento de dependencias y la posibilidad de trabajar en equipo o desplegar en servidores remotos.

Se recomienda comenzar por la versión local para familiarizarse con la estructura de Airflow, la definición de DAGs y el flujo de ejecución básico. Luego, avanzar a la versión con Docker para entender cómo escalar y mantener Airflow de forma robusta, portátil y reproducible en distintos entornos.

