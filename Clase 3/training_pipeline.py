import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("data.csv")

model = LinearRegression()
model.fit(df[["event_1"]], df["revenue"])
print("fIT FINISH")
filename = 'model_fi.sav'
pickle.dump(model, open(filename, 'wb'))
