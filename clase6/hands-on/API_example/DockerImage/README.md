# Version de API contenizada

Ahora podemos construir nuestra version contenizada de la API que veniaos trabajando con FastAPI.

## 1. Crear la imagen de Docker

Para construir la imagen de Docker, necesitas ejecutar el comando docker build. Este comando lee el archivo Dockerfile en el directorio actual, instala las dependencias y empaqueta la aplicación.

Abre una terminal en esta ruta y ejecuta:

```bash
docker build -t mi-api-fastapi .
```

- `docker build`: El comando para construir la imagen.
- `-t mi-api-fastapi`: Asigna un nombre (tag) a la imagen. Puedes cambiar mi-api-fastapi al que prefieras.
- `.`: Le indica a Docker que el Dockerfile está en el directorio actual.

## 2. Ejecutar el contenedor

Una vez que la imagen está lista, puedes iniciar un contenedor a partir de ella. El siguiente comando lanzará la aplicación en segundo plano y mapeará el puerto del contenedor al de tu máquina.

```bash
docker run -d --name mi-contenedor-fastapi -p 8000:8000 mi-api-fastapi
```

- `docker run`: Inicia un nuevo contenedor.
- `-d`: Corre el contenedor en modo detached (en segundo plano).
- `--name mi-contenedor-fastapi`: Le da un nombre a tu contenedor para que sea más fácil gestionarlo.
- `-p 8000:8000`: Mapea el **puerto 8000** de tu máquina al **puerto 8000** dentro del contenedor.
- `mi-api-fastapi`: El nombre de la imagen que creaste en el paso anterior.

## 3. Probar la API

Una vez que el contenedor está en ejecución, puedes acceder a la API desde tu navegador o con una herramienta como curl o Postman.

### Documentación interactiva

Puedes ver la documentación interactiva de la API (Swagger UI) y probar los endpoints desde tu navegador: [http://localhost:8000/docs](http://localhost:8000/docs)

### Endpoint de predicción

Puedes enviar una solicitud POST al endpoint /predict/ con los datos de un animal para obtener una predicción.

```
URL: http://localhost:8000/predict/
Método: POST
Headers:
api_key: test-key
Content-Type: application/json
```

#### Cuerpo de la solicitud (JSON):

```json
{
  "size": 25,
  "height": 30.3,
  "weight": 8,
  "number_of_whiskers": 12
}
```