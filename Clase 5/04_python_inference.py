import requests

def externalized_model(request) -> list:


    vm_ip =  #By default the internal one is 127.0.0.1

    headers = {}
    json_data = request.get_json()

    response = requests.post(f'http://{vm_ip}:5000/invocations', headers=headers, json=json_data)
    return str(response.json())

#print(make_inference([[0,0,0,0],[1,1,1,1]]))
