import requests

def make_inference(data) -> list:

    headers = {
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
    }

    json_data = {
    'data': data
    }

    response = requests.post('http://127.0.0.1:5000/invocations', headers=headers, json=json_data)
    return response.json()


print(make_inference([[0,0,0,0],[1,1,1,1]]))

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{  "data": [ [0,0,0,0]]}'
#response = requests.post('http://127.0.0.1:5000/invocations', headers=headers, data=data)
