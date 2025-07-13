# Hands-on - Gestión de Modelos con MLFlow

En el mundo del Aprendizaje Automático, crear modelos es solo el primer paso. A medida que desplegamos más modelos en producción, gestionarlos de manera efectiva se vuelve crucial. Este proceso, conocido como MLOps, se encarga de garantizar que los modelos se desplieguen, supervisen y actualicen de forma eficiente y confiable. En este sentido, MLFlow surge como una herramienta clave para facilitar este proceso.

Este *hands-on* tiene como objetivo explorar el uso de MLFlow en el desarrollo y operación de modelos de aprendizaje automático. Descubriremos cómo MLFlow permite realizar seguimiento de experimentos, registrar modelos e implementarlos en producción, brindándonos una plataforma integral para gestionar todo el ciclo de vida de los modelos.

Vamos a dividir este *hands-on* en dos formas de ejecutar MLFlow:

- Gestión de modelos con MLFlow en ejecución local — carpeta `local_version`
- Gestión de modelos con MLFlow en contenedor Docker — carpeta `container_version`

Ambas formas son muy similares en funcionalidad, pero difieren en la forma en que se instalan y gestionan los servicios:

- La versión local es ideal para desarrollos rápidos, pruebas individuales o uso en notebooks, ya que MLFlow se ejecuta directamente en tu entorno virtual o sistema. Es fácil de instalar y ejecutar, pero depende del entorno de cada usuario (lo cual puede generar inconsistencias entre equipos).

- La versión dockerizada encapsula toda la infraestructura de MLFlow (servidor, base de datos y almacenamiento de artefactos) en contenedores, lo cual facilita la portabilidad, escalabilidad y reproducibilidad del entorno. Es más cercana a un entorno de producción real y permite que múltiples personas accedan a un servicio centralizado.

Se recomienda comenzar por la versión local para familiarizarse con los conceptos, y luego avanzar a la versión con Docker para entender cómo escalar y mantener MLFlow en un entorno más robusto.
