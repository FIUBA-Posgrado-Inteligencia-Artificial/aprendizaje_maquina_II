# Ejecución de los contenedores

Si queremos usar la línea de comando, los pasos a seguir es

1. Construimos las imágenes y levantamos todo

```Bash
docker-compose up -d
```

2. Para bajar todo hacemos:

```Bash
docker compose down 
```

3. Si queremos eliminar las imágenes y los volúmenes, hacemos

```Bash
docker compose down --rmi all --volumes
```