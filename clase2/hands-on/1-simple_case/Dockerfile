# Partimos de una imagen base de Python https://hub.docker.com/_/python
FROM python:3.13-slim
LABEL authors="facundolucianna"

# Agregamos el codigo al contenedor
ADD main.py ./main.py

# Definimos un punto de entrada a la imagen
#ENTRYPOINT ["python", "main.py"]
CMD ["python", "main.py"]
