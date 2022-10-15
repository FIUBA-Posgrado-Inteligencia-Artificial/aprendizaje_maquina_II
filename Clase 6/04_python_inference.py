import requests
from sqlalchemy import create_engine



def externalized_model(request) -> list:


    #check this question to know the parameters https://stackoverflow.com/questions/3582552/what-is-the-format-for-the-postgresql-connection-string-url
    engine = create_engine('postgresql+psycopg2://postgres:?)T"L.GYq~FUdn]d@34.172.137.45:5432/postgres')
    connection = engine.connect()

    vm_ip = '0.0.0.0' #By default the internal one is 127.0.0.1

    headers = {}
    #json_data = request.get_json()
    json_data = request

    response = requests.post(f'http://{vm_ip}:5000/invocations', headers=headers, json=json_data)
    response = response.json()
    predicted_value = response[0]
    
    connection.execute(f"INSERT INTO public.inferecence (id_event,predicted_value,true_value) VALUES ('0',{predicted_value},-1)")
    return str(response)

print(externalized_model({"data":[[10,10,10,50]]}))
