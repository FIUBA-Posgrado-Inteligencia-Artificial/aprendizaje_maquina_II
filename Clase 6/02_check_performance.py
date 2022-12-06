import requests
from sqlalchemy import create_engine

#Initial config
vm_ip   =  #By default the internal ip used by mlflow is 127.0.0.1, but to externalize the model the external  ip of the vm must be written here
db_pass = 
db_ip   = 
db_name = 


def get_ground_truth():

    with create_engine(f'postgresql+psycopg2://postgres:postgres@localhost:5432/db1') as engine:
            truth_data = engine.execute('select * from mlops.ground_truth').fetchall()

    truth_data = pd.DataFrame(data, columns=['event_id', 'true_value'])

    return truth_data

def get_predictions():

    with create_engine(f'postgresql+psycopg2://postgres:postgres@localhost:5432/db1') as engine:
            predicted_data = engine.execute('select * from mlops.inference').fetchall()

    predicted_data = pd.DataFrame(data, columns=['event_id', 'predicted_value'])

    return predicted_data


def save_performance(business_metrics):


def measure_performance(df_measures):
    "Here we'll measure just the RMSE"
    MAE = (df_measures["true_value"] - df_measures["predicted_value"]).abs().mean()
    MSE = ((df_measures["true_value"] - df_measures["predicted_value"])**2).mean()



    return MAE, MSE

if __name__ == '__main__':
    df_ground_truth = get_ground_truth()
    df_predictions  = get_predictions()

    #Could this be done in the SQL engine, yes
    #Will I do that? No
    df_measures = df_ground_truth.merge(df_predictions)

    business_metrics = measure_performance(df_measures)
    save_performance(business_metrics)

