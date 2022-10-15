#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mlflow
from mlflow.client import MlflowClient

import os
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy  as np
from numpy import random as rd
from matplotlib import pyplot as plt


from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV

import pandas as pd


#This will be used in the next class
os.chdir('/home/ml2/aprendizaje_maquina_II/Clase 5') 


## This db could be an external postgres database
mlflow.set_tracking_uri('sqlite:///mlruns.db')

## This will fail in databricks because the experiment_id is a random hash

new_experiment_id = 0 #Why not put this in an else? Just because I can
list_mlflow_experiments =  mlflow.search_experiments()
if len(list_mlflow_experiments):
    list_experiment_id = list(map(lambda list_mlflow_experiments: int(list_mlflow_experiments.experiment_id), list_mlflow_experiments ))
    last_experiment_id =  max(list_experiment_id)
    new_experiment_id  = last_experiment_id + 1
    
    mlflow.create_experiment(str(new_experiment_id))


# This should be a query from a database
X = sklearn.datasets.load_iris().data
y = sklearn.datasets.load_iris().target


# # Usando el autolog muchas metricas se guardan solas...

# In[3]:


mlflow.sklearn.autolog(max_tuning_runs = None)

X_train, X_test, y_train, y_test = train_test_split(X,y)


# In[4]:


def log_model(model,
              developer = None,
              experiment_id = None,
              grid = False,
              **kwargs):
    
    
    assert developer     is not None, 'You must define a developer first'
    assert experiment_id is not None, 'You must define a experiment_id first'
    
    
    with mlflow.start_run(experiment_id = experiment_id):

        mlflow.set_tag('developer',developer)
        
        #The default is to train just one model
        model = model(**kwargs)
        if grid:
            model = GridSearchCV(model,param_grid = kwargs)
        
        
        
        model.fit(X_train, y_train)
        test_acc = (model.predict(X_test) == y_test).mean()

        mlflow.log_metric('test_acc',test_acc)


# In[5]:


#normal logging
log_model(DecisionTreeClassifier,'camilo', experiment_id = new_experiment_id)
log_model(LogisticRegression    ,'camilo', experiment_id = new_experiment_id, **{'max_iter':1000})
log_model(SVC                   ,'camilo', experiment_id = new_experiment_id, **{'C':0.001,'class_weight':'balanced'})

#grid logging
log_model(SVC    ,
          'camilo', 
          experiment_id = new_experiment_id, 
          grid = True,
          **{'kernel':('linear', 'rbf'), 'C':[1, 10]}
)

