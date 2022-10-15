import mlflow 
import sklearn

experiment_id = '0'
model_registry_uri = '/mlruns.db'

mlflow.set_tracking_uri('sqlite:///mlruns.db')
mlflow.set_registry_uri('sqlite://' + model_registry_uri)


runs = mlflow.search_runs(experiment_ids = [experiment_id])

best_model_run_id = runs.sort_values(by = ['metrics.test_acc'], ascending = False).iloc[0]['run_id']

mlflow.register_model(f'runs:/{best_model_run_id}/model','ml2_uba')

