import requests
from sqlalchemy import create_engine
from sqlalchemy import text

# Initial config
vm_ip =  "127.0.0.1"# By default the internal ip used by mlflow is 127.0.0.1, but to externalize the model the external  ip of the vm must be written here
vm_port = "5001"

db_pass = "postgres"
db_ip = "localhost"
db_name = "postgres"
db_user = "postgres"
db_port = "5432"


def parse_request(request):
    # The request MUST have this format
    # {'dataframe_split': {event_id: '5e82b70d-b550-4bee-9d5d-16a2e73029f9', 'data':[[10,10,10,10]]}}
    request = request.get_json()

    event_id = request.pop('event_id') if 'event_id' in request else 'no_event_id'

    features = request["data"][0]

    assert len(request["data"] == 1, "We want to have just one inference at the time")
    assert len(features) == 4, 'The request must have the correct ammount of columns (At least)'

    return event_id, features


def save_predictions(event_id, prediction):
    # For remote dbs
    # engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_ip}:{db_port}/{db_name}')

    # For localhost there is no port
    # engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_ip}/{db_name}')

    sql_insert = f"INSERT INTO public.inference (event_id, predicted_value) VALUES ({event_id},'{prediction}')"
    with engine.begin() as connection:
        connection.execute(text(sql_insert))


def externalized_model(features) -> str:
    headers = {}

    json_request =  {'dataframe_split': {'data':[features]}}

    response = requests.post(f'http://{vm_ip}:{vm_port}/invocations', headers=headers, json=json_request)
    response = response.json()["predictions"]

    return response[0]


def check_business_logic(features):
    """
    Here We should put some business logic
    We're going to put the min/max of the iris dataset features
    """
    sepal_length, sepal_width, petal_length, petal_width = features

    sepal_length_condition = (4.3 <= sepal_length) and (sepal_length <= 7.9)
    sepal_width_condition = (2.0 <= sepal_width) and (sepal_width <= 4.4)
    petal_length_condition = (1.0 <= petal_length) and (petal_length <= 6.9)
    petal_width_condition = (0.1 <= petal_width) and (petal_width <= 2.5)

    return sepal_length_condition and sepal_width_condition and petal_length_condition and petal_width_condition


def get_business_prediction(features):
    "Here we could have some function of the feature"

    return -1


def trigger_events(request):
    # This pipeline supposes that we are using it to do just one inference at the time
    # If we want to do more inferences, we need to modify the functions to be able to handle them

    event_id, features = parse_request(request)

    if check_business_logic(features):
        prediction = get_business_prediction(features)

    else:
        prediction = externalized_model(features)

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
