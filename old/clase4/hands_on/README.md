# Hands-on - Usando Apache Airflow para Sincronización de Tareas

En el mundo de los flujos de trabajo y la sincronización de tareas, Apache Airflow es una herramienta ampliamente utilizada. Más allá de la simple ejecución de tareas, Airflow permite la creación, planificación y monitoreo de flujos de trabajo complejos.

En este *hands-on*, exploraremos cómo utilizar Apache Airflow para la sincronización de tareas en el contexto de procesos de datos. Crearemos un DAG para un proceso ETL, abordando tanto la implementación con TaskFlow como la definición de DAGs de manera más tradicional.

Dividiremos este *hands-on* en dos formas de ejecutar Airflow:

- Usando Apache Airflow en modo local — carpeta `local_version`
- Usando Apache Airflow con servicio dockerizado — carpeta `container_version`

Ambas formas ofrecen una funcionalidad similar, pero difieren en la instalación y la gestión de los servicios:

- **Versión local**: Ideal para entornos de desarrollo o pruebas individuales, donde se ejecuta Airflow directamente en un entorno virtual o en el sistema del usuario. Es simple de configurar, rápida para comenzar y útil para comprender los conceptos básicos sin depender de contenedores ni redes. 

- **Versión dockerizada**: Encapsula toda la infraestructura de Airflow (scheduler, webserver, worker, base de datos, etc.) dentro de contenedores Docker, permitiendo una ejecución más cercana a un entorno de producción. Esto facilita la portabilidad, el aislamiento de dependencias y el trabajo colaborativo o en servidores remotos.

Se recomienda comenzar por la versión local para familiarizarse con la estructura de Airflow, la definición de DAGs y el flujo de ejecución básico. Luego, avanzar a la versión con Docker para entender cómo escalar y mantener Airflow de forma robusta, portátil y reproducible en distintos entornos.

## Variante local usando MetaFlow

Dado que ejecutar Apache Airflow en local puede resultar algo pesado o complejo para algunas configuraciones, también se incluye una alternativa utilizando [MetaFlow](https://metaflow.org/) — una herramienta de código abierto desarrollada por Netflix para el desarrollo y orquestación de flujos de trabajo de ciencia de datos.

MetaFlow permite definir flujos de tareas mediante Python puro, sin necesidad de escribir código específico para una interfaz web o YAML. Su enfoque es centrado en el desarrollador, simple de usar y orientado a entornos tanto locales como en la nube.

Para acceder a este hands-on, ir a la carpeta `local_metaflow`