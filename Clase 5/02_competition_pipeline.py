import mlflow 
from mlflow.client import MlflowClient

import os

#This will be used in the next class
os.chdir('/home/ml2/aprendizaje_maquina_II/Clase 5')

model_registry_uri = '/mlruns.db'
mlflow.set_tracking_uri('sqlite:///mlruns.db')
mlflow.set_registry_uri('sqlite://' + model_registry_uri)


list_mlflow_experiments =  mlflow.search_experiments()
list_experiment_id = list(map(lambda list_mlflow_experiments: int(list_mlflow_experiments.experiment_id), list_mlflow_experiments ))
last_experiment_id =  max(list_experiment_id)


runs = mlflow.search_runs(experiment_ids = [last_experiment_id])

best_model_run_id = runs.sort_values(by = ['metrics.test_acc'], ascending = False).iloc[0]['run_id']
print(best_model_run_id)

new_model = mlflow.register_model(f'runs:/{best_model_run_id}/model','ml2_uba')


client = mlflow.client.MlflowClient()
client.transition_model_version_stage('ml2_uba',
                                      new_model.version,
                                      "production",
                                      archive_existing_versions = True)


