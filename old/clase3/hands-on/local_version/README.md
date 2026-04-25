# Hands-on - Gestión de Modelos con MLFlow mediante en Local

En el mundo del Aprendizaje Automático, crear modelos es solo el primer paso. A medida que desplegamos más modelos en producción, gestionarlos de manera efectiva se vuelve crucial. Este proceso, conocido como MLOps, se encarga de garantizar que los modelos se desplieguen, supervisen y actualicen de forma eficiente y confiable. En este sentido, MLFlow surge como una herramienta clave para facilitar este proceso.

Este *hands-on* tiene como objetivo explorar el uso de MLFlow en el desarrollo y operación de modelos de aprendizaje automático. Descubriremos cómo MLFlow permite realizar seguimiento de experimentos, registrar modelos e implementarlos en producción, brindándonos una plataforma integral para gestionar todo el ciclo de vida de los modelos.

## Ejecución en local de MLFlow

Para realizar este hands-on, necesitás tener instalado MLFlow en tu máquina local. Para ello, vamos a instalar la librería `mlflow` dentro de un entorno virtual.

Este ejemplo está pensado para `conda`, pero se puede utilizar cualquier gestor de entornos virtuales y paquetes (como `venv`, `pipenv`, `poetry`, etc.).

1 - Activamos el entorno virtual (o creamos uno nuevo)

```Bash
conda activate proyect_env
```

2 - Instalamos MLFlow

```Bash
conda install --y mlflow
```

> También podés usar `pip install mlflow` si estás trabajando con un entorno virtual distinto.

3 - Ejecutamos MLFlow dentro del entorno. Es importante ubicarse en el directorio donde deseamos que MLFlow almacene sus datos.
```Bash
mlflow server --host 127.0.0.1 --port 8888
```

4 - Accedemos a la interfaz web. Abrimos el navegador y vamos a: [http://127.0.0.1:8080](http://127.0.0.1:8080)

### Observaciones importantes

**OBS1:** Es fundamental elegir correctamente la carpeta desde la cual ejecutamos MLFlow de manera local, ya que en ese lugar se generarán carpetas como `mlruns` y `mlartifacts`, que almacenan toda la información relacionada con los experimentos, artefactos y modelos registrados. Si más adelante querés continuar el trabajo o visualizar lo que ya hiciste, deberás volver a ejecutar MLFlow desde ese mismo directorio. Si se eliminan esas carpetas se perderá el historial completo, o si se ejecuta desde otra ubicación, no se verá nada de lo ejecutado anteriormente.

**OBS2:** También podés instalar MLFlow globalmente en tu sistema (fuera de un entorno virtual) usando herramientas como:
    - `pipx install mlflow`
    - `uv tool install mflow`

Estas opciones instalan MLFlow de forma aislada, permitiéndote ejecutarlo como una herramienta de línea de comandos sin necesidad de activar un entorno cada vez. Es útil si lo vas a usar frecuentemente desde distintas ubicaciones.

**OBS3:** Cuando ejecutás el servidor de MLFlow, podés personalizar la ubicación de sus archivos de almacenamiento (por ejemplo, usando `--backend-store-uri` y `--artifacts-destination`) para tener una estructura centralizada y de fácil mantenimiento. Podés encontrar más opciones de configuración avanzada en la [documentación oficial de MLFlow](https://mlflow.org/docs/latest/cli.html#mlflow-server)