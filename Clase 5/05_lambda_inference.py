import requests
def externalized_model(request) -> str:
    vm_ip =   # By default the internal ip used by mlflow is 127.0.0.1, but to externalize the model the external  ip of the vm must be written here

    headers = {}

    request = request.get_json()
    # The request MUST have this format
    # {'dataframe_split': {'data':[[10,10,10,10],[0,0,0,0]]}}

    response = requests.post(f'http://{vm_ip}:5001/invocations', headers=headers, json=request)
    return str(response.json())