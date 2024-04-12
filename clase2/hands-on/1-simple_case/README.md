# Instalación de la imagen

Si queremos usar la linea de comando, los pasos a seguir es

1. Construimos la imagen

```Bash
docker build -t python-app:latest . 
```

2. Ahora podemos ejecutar la imagen.

```Bash
docker run python-app
```