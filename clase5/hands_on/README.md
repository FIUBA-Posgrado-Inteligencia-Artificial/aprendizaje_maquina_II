# Hands-on - Batch Processing

![Diagrama de servicios](redis_batch.png)

En este *hands-on*, vamos a ver un caso de procesamiento por lotes (Batch Processing). Para ello, utilizamos los datos del [Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) y un modelo de [XGBoost](https://xgboost.readthedocs.io/en/stable/) previamente entrenado.

Una vez obtenidas las predicciones, se almacenan en una base de datos Valkey, ya que buscamos una respuesta de baja latencia para conocer la salida de los datos. Si bien el ejemplo no es ideal por el tipo de entradas, este tipo de base de datos es óptima cuando manejamos datos de usuarios identificables, permitiendo almacenar las predicciones junto a un ID de usuario y otros datos relevantes.

La implementación se compone de una parte que corre localmente y otra que se ejecuta con Docker Compose.

## Docker Compose

Para este ejemplo, se levantan dos servicios:

- [MinIO](https://min.io/): Con este servicio simulamos el uso de un bucket S3 de Amazon. En este caso, se crea un bucket llamado `batch`, que contiene los datos a predecir y el artefacto del modelo entrenado.
- [Valkey](https://valkey.io/): Valkey es un motor de base de datos en memoria, basado en almacenamiento mediante tablas hash.

Para levantar los servicios, desde la raíz del repositorio ejecutar:

```bash
docker compose up
```

## Ejecución Local

Para la ejecución local se cuenta con:

- Un DAG de Metaflow, diseñado para realizar predicciones por lotes utilizando un modelo previamente entrenado. El DAG `batch_processing.py` se encuentra en el directorio `metaflow`.
- Un notebook para testear Valkey, que establece una conexión con el servidor utilizando la biblioteca de Python compatible (redis-py). Luego, recupera las predicciones almacenadas en Valkey utilizando las claves generadas previamente.

> Nota: Para que tanto el DAG como el notebook funcionen correctamente, los servicios de Docker deben estar levantados.

### Estructura del DAG

El DAG consta de los siguientes pasos:

- `start`: Inicia el flujo e imprime un mensaje de comienzo. Luego avanza a cargar los datos y el modelo.
- `load_data`: Carga los datos de entrada desde un bucket S3 utilizando Metaflow, y los guarda en un DataFrame de pandas.
- `load_model`: Carga el modelo entrenado desde el bucket S3 y lo instancia como un objeto XGBClassifier.
- `batch_processing`: Realiza las predicciones en lote utilizando el modelo cargado. Para cada fila genera un hash y almacena las predicciones en un diccionario.
- `ingest_valkey`: Ingresa las predicciones en Valkey utilizando la biblioteca de Python compatible (redis-py). Establece conexión con el servidor y guarda las predicciones.
- `end`: Imprime un mensaje de finalización del flujo.

Este *hands-on* fue desarrollado con Python 3.11, aunque debería funcionar sin problemas en versiones >= 3.9. Los requerimientos están listados en `requirements.txt`.

```bash
python3 ./metaflow/batch_processing.py run
```

## Apagar los servicios

Estos servicios consumen memoria y recursos del sistema, por lo que se recomienda detenerlos cuando no estén en uso. Para ello, ejecutar:

```bash
docker compose down
```

Si deseas eliminar también las imágenes y los volúmenes (esto borra todos los datos), ejecuta:

```bash
docker compose down --rmi all --volumes
```

> Nota: Esto eliminará todo el contenido de los buckets y la base de datos Valkey. Usar con precaución.
