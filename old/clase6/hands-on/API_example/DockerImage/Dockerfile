FROM python:3.11-slim

# Setea el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos e instálalos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de la aplicación al contenedor
COPY . .

# Expone el puerto en el que va a correr la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]