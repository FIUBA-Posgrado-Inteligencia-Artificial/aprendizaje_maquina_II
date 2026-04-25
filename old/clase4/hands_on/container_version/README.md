# Hands-on - Usando Apache Airflow para Sincronización de Tareas mediante servicio dockerizado

En el mundo de los flujos de trabajo y la sincronización de tareas, Apache Airflow es una herramienta ampliamente utilizada. Más allá de la simple ejecución de tareas, Airflow permite la creación, planificación y monitoreo de flujos de trabajo complejos.

En este *hands-on*, exploraremos cómo utilizar Apache Airflow para la sincronización de tareas en el contexto de procesos de datos. Crearemos un DAG para un proceso ETL, abordando tanto la implementación con TaskFlow como la definición de DAGs de manera más tradicional.

## Ejecución con Docker Compose

Para realizar este *hands-on*, es necesario tener disponible el servicio de Apache Airflow tal como está definido en el archivo de Docker Compose. Antes de ejecutar estas imágenes de Docker, asegúrate de crear las carpetas `config`, `logs` y `plugins` dentro de la carpeta `airflow` que se encuentra en este *hands-on*.

Para ejecutar Docker Compose:

```Bash
docker compose up
```
Una vez que se inicializa, podrás acceder a Airflow en `http://localhost:8080` e ingresar con usuario/contraseña: `airflow/aiflow`.

Para detener el servicio:
```Bash
docker compose down
```

Para detenerlo y eliminar todo:
```Bash
docker compose down --rmi all --volumes
```
