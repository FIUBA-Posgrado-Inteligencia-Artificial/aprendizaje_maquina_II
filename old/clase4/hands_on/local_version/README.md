# Hands-on - Usando Apache Airflow para Sincronización de Tareas mediante servicio modo local

En el mundo de los flujos de trabajo y la sincronización de tareas, Apache Airflow es una herramienta ampliamente utilizada. Más allá de la simple ejecución de tareas, Airflow permite la creación, planificación y monitoreo de flujos de trabajo complejos.

En este *hands-on*, exploraremos cómo utilizar Apache Airflow para la sincronización de tareas en el contexto de procesos de datos. Crearemos un DAG para un proceso ETL, abordando tanto la implementación con TaskFlow como la definición de DAGs de manera más tradicional.

## Ejecución local de Airflow

Para realizar este *hands-on*, es necesario instalar Airflow de forma local. Siguiendo [las instrucciones oficiales de Apache Airflow](https://airflow.apache.org/docs/apache-airflow/2.3.0/start/local.html), se creó un script en bash que automatiza la instalación y configuración para que todo funcione correctamente:

1. Instala `airflow` usando `uv`, `pipx` o `venv`. Apache Airflow recomienda `uv`.
1. Crea la carpeta `airflow` para que Apache Airflow pueda almacenar su contenido. Por defecto es `~/airflow`, pero puede modificarse según conveniencia.
1. Copia los DAGs que tenemos en la carpeta `dags` a la carpeta de Airflow.
1. Copia el archivo `conf/airflow` y además configurandolo agregando información de paths necesaria.

> Este script se validó su funcionamiento en Linux (Arch) y macOS. Falta ver si funciona en Windows con WSL, se valora contribución de verificar si este funciona en Windows, o un script exclusivo para ese OS.

Para ejecutar este instalador (`install_locally.sh`), haz lo siguiente:

```Bash
chmod +x ./install_locally.sh
./install_locally.sh
```
Una vez instalada la aplicación, puedes inicializar Airflow usando el script `run_locally.sh` (es importante estar dentro del entorno virtual donde se instaló Apache Airflow):

```Bash
chmod +x ./run_locally.sh
./run_locally.sh
```
Una vez que se inicialice, podrás acceder a Airflow ingresando a `http://localhost:8080`