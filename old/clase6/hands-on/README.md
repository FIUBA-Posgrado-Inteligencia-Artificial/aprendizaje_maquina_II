# FastAPI Example with Uvicorn

Este hands-on demuestra cómo crear un servicio simple de aprendizaje automático utilizando FastAPI y ejecutarlo con 
Uvicorn.

## Uso

1. Inicia el servicio de FastAPI con Uvicorn (puede usar cualquiera de los main):

```Bash
uvicorn main_1:app --host 0.0.0.0 --port 80
```

2. El servicio estará disponible en http://127.0.0.1:8000.

3. Para hacer predicciones, envía una solicitud POST a http://127.0.0.1:8000/predict/ con los datos de entrada 
requeridos. Los datos de entrada deben incluir valores para los features utilizadas para la clasificación.

## ¿Por qué Uvicorn?

Uvicorn es un servidor [ASGI](https://asgi.readthedocs.io/en/latest/) extremadamente rápido que está diseñado para 
funcionar perfectamente con FastAPI. FastAPI en sí mismo es un framework moderno para construir API con Python que se 
basa en sugerencias de tipos estándar de Python. Uvicorn proporciona un alto rendimiento y admite el manejo asíncrono 
de solicitudes, lo que lo convierte en una elección ideal para ejecutar aplicaciones FastAPI.
