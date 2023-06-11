import requests 

new_measurement = {
    'sepal_length': 5.7,
    'sepal_width': 3.1,
    'petal_length': 4.9,
    'petal_width': 2.2
}

response = requests.post('http://127.0.0.1:8000/predict', json=new_measurement)
print(response.content)