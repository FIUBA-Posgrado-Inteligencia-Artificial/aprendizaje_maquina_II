import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class QCutTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, column, num_bins, labels):
        self.column = column
        self.num_bins = num_bins
        self.labels = labels
        self.bins = None
    
    def fit(self, X, y=None):
        self.bins = pd.qcut(X[self.column], q=self.num_bins, labels=self.labels).unique()
        return None
    
    def transform(self, X):
        X[self.column+'_qcut'] = pd.cut(X[self.column], bins=self.bins, labels=self.labels, include_lowest=True)
        return X
    

if __name__ == '__main__':
    from sklearn.pipeline import Pipeline

    pipeline = Pipeline([
        ('qcut', QCutTransformer(column='Item_MRP', num_bins=4, labels = [1, 2, 3, 4])),
        # Otros pasos del pipeline
    ])
