# Hands-on - Gestión de Modelos con MLFlow

En el mundo del Aprendizaje Automático, crear modelos es solo el primer paso. A medida que desplegamos más modelos en 
producción, gestionarlos de manera efectiva se vuelve crucial. Este proceso, conocido como MLOps, se encarga de 
garantizar que los modelos se desplieguen, supervisen y actualicen de manera eficiente y confiable. En este sentido, 
MLFlow surge como una herramienta que ayuda en este proceso.

Este hands-on de MLFlow tiene como objetivo explorar su utilidad en el día a día del desarrollo de Aprendizaje 
Automático y operaciones de modelos (MLOps). Descubriremos cómo MLFlow facilita el seguimiento de experimentos, el 
registro de modelos y la implementación en producción, brindándonos una plataforma integral para gestionar todo el 
ciclo de vida de nuestros modelos.

## Ejecución de Docker Compose

Para poder realizar este hands-on, necesitamos tener disponible el servicio de MLFlow tal como está definido 
en el archivo de Docker Compose. 

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
