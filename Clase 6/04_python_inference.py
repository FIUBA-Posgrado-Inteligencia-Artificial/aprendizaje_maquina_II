import requests
from sqlalchemy import create_engine

import requests

def externalized_model(request) -> list:


    vm_ip =  #By default the internal one when using mlflow is 127.0.0.1, but here the external ip of the vm must be written

    headers = {}
    json_data = request.get_json()

    response = requests.post(f'http://{vm_ip}:5000/invocations', headers=headers, json=json_data)
    return str(response.json())

#print(make_inference([[0,0,0,0],[1,1,1,1]]))

def externalized_model(request) -> list:

    #vm data
    vm_ip =  #By default the internal one when using mlflow is 127.0.0.1, but here the external ip of the vm must be written

    #db data
    db_pass = #To be completed
    db_ip = #To be completed
    db_name = #To be completed


    #Run the inference
    headers = {}
    json_data = request.get_json()
    #json_data = request #If we are testing in the vm we must pass an already parsed dict

    response = requests.post(f'http://{vm_ip}:5000/invocations', headers=headers, json=json_data)
    response = response.json()
    predicted_value = response[0] #This is assuming we use the model to do one inference at the time
    

    #check this question to know the connection string works
    #https://stackoverflow.com/questions/3582552/what-is-the-format-for-the-postgresql-connection-string-url
    engine = create_engine(f'postgresql+psycopg2://postgres:{df_pass}@{db_ip}:5432/{db_name}')
    connection = engine.connect()
    
    #Here the values to be saved depends on the bussiness
    connection.execute(f"INSERT INTO public.inferecence (id_event,predicted_value,true_value) VALUES ('0',{predicted_value},-1)")
    
    return str(response)

#To check in the vm
#print(externalized_model({"data":[[10,10,10,50]]}))
