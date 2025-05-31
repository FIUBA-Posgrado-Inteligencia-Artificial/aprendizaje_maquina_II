# Partimos de una imagen base de Python https://hub.docker.com/_/python
FROM python:3.13-slim
LABEL authors="facundolucianna"

# Agregamos requirement.txt al contenedor e instalamos los requerimientos
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copiamos lo que esta en esta carpeta a app del contenedor
COPY . /app
# Establecemos como la carpeta de trabajo a app
WORKDIR /app

# Definimos un punto de entrada a la imagen
ENTRYPOINT ["python"]
CMD ["app.py"]