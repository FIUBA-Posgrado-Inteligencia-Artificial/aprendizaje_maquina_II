import requests
from sqlalchemy import create_engine
from sqlalchemy import text

#Initial config
vm_ip   =  #By default the internal ip used by mlflow is 127.0.0.1, but to externalize the model the external  ip of the vm must be written here
vm_port = "5001"

db_pass = 
db_ip   = 
db_name =
db_user =
db_port =


def check_business_logic(request_data):
    """We are supposing that we want to predict
    the total ammount of a loan por an user, and the first columns is the date,
    so we wan't to reject it always"""

    age = request_data["dataframe_split"]["data"][0][0]

    return age > 18

def parse_request(request):

    #This is to be able to check the lambda fn inside the vm
    if type(request) is not dict:
        #The request MUST have this format
        # {'dataframe_split': {'data':[[10,10,10,10],[0,0,0,0]]}}
        request = request.get_json()
       
    event_id = request.pop('event_id') if 'event_id' in request else 'no_event_id' 

    return event_id , request




def save_predictions(event_id, prediction):

    # For remote dbs
    # engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_ip}:{db_port}/{db_name}')

    # For localhost there is no port
    # engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_ip}/{db_name}')

    sql_insert = f"INSERT INTO public.inference (event_id, predicted_value) VALUES ({event_id},'{prediction}')"
    with engine.begin() as connection:
        connection.execute(text(sql_insert))



def externalized_model(request) -> str:

    headers = {}

    response = requests.post(f'http://{vm_ip}:{vm_port}/invocations', headers=headers, json=request)
    response = response.json()["predictions"]

    assert len(response_prediction) == 1, 'I want to have just one inference'

    return response[0]



def trigger_events(request):

    #This pipeline supposes that we are using it to do just one inference at the time
    #If we want to do more inferences, we need to modify the functions to be able to handle them

    event_id, request_data = parse_request(request)

    if check_business_logic(request_data):
        prediction = externalized_model(request_data)
    else:
        #This is the default custom amount
        #We could writte any value here that makes business sense
        prediction = 0.0
    save_predictions(event_id, prediction)

    return prediction


#print(trigger_events(
#   {"event_id": "event_id_2", "dataframe_split": {"data":[[0,0,0,0]]}}
#    ))


#print(trigger_events(
#    {"event_id": "event_id_1", "dataframe_split": {"data":[[10,10,10,10]]}}
#    ))

#print(trigger_events(
#    { "dataframe_split": {"data":[[0,0,0,0]]}}
#    ))

#print(trigger_events(
#    { "dataframe_split": {"data":[[19,10,10,10]]}}
#    ))
