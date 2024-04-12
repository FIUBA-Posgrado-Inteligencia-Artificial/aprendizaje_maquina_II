# Instalación de la imagen

Si queremos usar la linea de comando, los pasos a seguir es

1. Construimos la imagen

```Bash
docker build -t hello-world-flask:latest . 
```

2. Ahora podemos ejecutar la imagen. Para esta imagen necesitamos conectar el puerto del host con el contendor asi 
podemos acceder.

```Bash
docker run -p 8000:8000 hello-world-flask
```