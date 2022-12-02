import requests
from sqlalchemy import create_engine

#Initial config
vm_ip   =  #By default the internal ip used by mlflow is 127.0.0.1, but to externalize the model the external  ip of the vm must be written here
db_pass = 
db_ip   = 
db_name = 

def parse_request(request):


    #This is to be able to check the lambda fn inside the vm
    if type(request) is not dict:
        #The request MUST have this format
        # {'dataframe_split': {'data':[[10,10,10,10],[0,0,0,0]]}}
        request = request.get_json()
       
    event_id = request.pop('event_id') if 'event_id' in request else 'no_event_id' 

    return event_id , request

def get_predictions(request_data):

    headers = {}


    response = requests.post(f'http://{vm_ip}:5000/invocations', headers=headers, json=request_data)
    response = response.json()
    response_prediction = response["predictions"]

    assert len(response_prediction) == 1, 'I want to have just one inference'

    return response_prediction[0]


def save_predictions(event_id, prediction):

    # check this question to know the connection string works
    # https://stackoverflow.com/questions/3582552/what-is-the-format-for-the-postgresql-connection-string-url
    engine = create_engine(f'postgresql+psycopg2://postgres:{db_pass}@{db_ip}:5432/{db_name}')
    connection = engine.connect()

    # Here the values to be saved depends on the business
    connection.execute(
        f"INSERT INTO public.inference (event_id,predicted_value) VALUES ('{event_id}',{prediction})"
    )


def trigger_events(request):

    #This pipeline supposes that we are using it to do just one inference at the time
    #If we want to do more inferences, we need to modify the functions to be able to handle them

    event_id, request_data = parse_request(request)
    prediction = get_predictions(request_data)
    save_predictions(event_id, prediction)

    return prediction


#print(trigger_events(
#    {"event_id": "asdadas", "dataframe_split": {"data":[[0,0,0,0]]}}
#    ))


#print(trigger_events(
#    { "dataframe_split": {"data":[[0,0,0,0]]}}
#    ))
