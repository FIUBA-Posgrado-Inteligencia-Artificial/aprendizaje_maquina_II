"""
data_handle.py

Function to test
"""
import pandas as pd
def import_data(pth):
    df = pd.read_csv(pth)
    return df
