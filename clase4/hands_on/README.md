# Hands-on - Usando Apache Airflow para Sincronización de Tareas

En el mundo del flujo de trabajo y la sincronización de tareas, Apache Airflow es una herramienta ampliamente 
utilizada. Más allá de la simple ejecución de tareas, Airflow permite la creación, planificación y monitoreo de flujos 
de trabajo complejos.

En este hands-on, exploraremos cómo utilizar Apache Airflow para la sincronización de tareas en el contexto de 
procesos de datos. Vamos a crear un DAG de un proceso ETL, explorando tanto la implementación con TaskFlow como la
definición de DAGs de manera más tradicional.

## Ejecución de Docker Compose

Para poder realizar este hands-on, necesitamos tener disponible el servicio de Apache Airflow tal como está definido 
en el archivo de Docker Compose. Antes de ejecutar estas imágenes de Docker, asegúrate de crear las carpetas 
`config`, `logs` y `plugins` dentro de la carpeta `airflow` que se encuentra en este hands-on.

Para ejecutar este docker compose:

```Bash
docker compose up
```

Para detenerlo:
```Bash
docker compose down
```

Para detenerlo y eliminar todo:
```Bash
docker compose down --rmi all --volumes
```
