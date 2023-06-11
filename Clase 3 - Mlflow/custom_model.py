import pandas as pd
import pickle
import cloudpickle
import mlflow
from mlflow.models import infer_signature
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import lightgbm as lgb
from sklearn.metrics import accuracy_score


class CustomModelPredictor(mlflow.pyfunc.PythonModel):
    """
    This Class define a custom model predictor to calculate something.

    It derives from the mlflow PythonModel base Class and has three
    main methods to work, fit, predict and load_context.
    """

    def __init__(self, var_features: list, target: str, model_params: dict):

        self.var_features = var_features
        self.target = target
        self.preprocessor = StandardScaler()
        self.model = lgb.LGBMClassifier(**model_params)

    def load_context(self, context) -> None:
        """
        This method will not be explicitly used in this module, but it is
        necessary for mlflow to understand how to load what has been
        trained further on, by loading the needed artifacts.

        :param context: A :class:`~PythonModelContext` instance containing artifacts that the model
                        can use to perform inference.
        """

        with open(context.artifacts["preprocessor"], "rb") as f:
            self.preprocessor = pickle.load(f)
        with open(context.artifacts["estimator"], "rb") as f:
            self.model = pickle.load(f)

        return None

    def fit(self, X_train, y_train) -> None:
        """
        This method will take a pandas DataFrame, fit the model, save that as a
        serialized pickle object and return the signature of the model

        :param data: the inputted DataFrame with the features of the model
        :type data: pd.DataFrame

        :return: signature of the model
        :rtype: ModelSignature
        """

        y = data.loc[:, self.target]
        X = data.drop(self.target, axis=1)
        X = X.loc[:, self.var_features]

        X_train, X_val, y_train, y_val = train_test_split(
            X, y, test_size=0.3, random_state=20, shuffle=True
        )

        # TRAINING THE PIPELINE

        # PREPROCESSOR FIT
        self.preprocessor.fit(X=X_train, y=y_train)

        # PREPROCESSOR TRANSFORM
        X_train_transformed = self.preprocessor.transform(X=X_train)

        # MODEL FIT
        self.model.fit(X_train_transformed, y_train)

        # MODEL EVALUATION AND LOGGING METRICS
        # Train metrics
        y_train_pred = self.model.predict(X_train_transformed)
        train_accuracy = accuracy_score(y_train_pred, y_train)
        mlflow.log_metric("train_accuracy", train_accuracy)

        # Validation metrics
        X_val_transformed = self.preprocessor.transform(X_val)
        y_val_pred = self.model.predict(X_val_transformed)
        val_accuracy = accuracy_score(y_val_pred, y_val)
        mlflow.log_metric("val_accuracy", val_accuracy)

        # Dumping the fitted objects
        with open("/path/to/fitted_model.pkl", "wb") as f:
            cloudpickle.dump(self.model, f)
        with open("/path/to/fitted_preprocessor.pkl", "wb") as f:
            cloudpickle.dump(self.preprocessor, f)

        # Inferring signature to return
        signature = infer_signature(X_train, self.predict(context="",X=X_train))

        return signature

    def predict(self,context, X: pd.DataFrame):
        """
        This method will evaluate a proper input with the loaded context
        and return the predicted output.

        :param X: the inputted DataFrame with the features of the model
        :type X: pd.DataFrame

        :return: probability predictions of the occurrence of the event given by the model
        :rtype: np.ndarray
        """
        X_transformed = self.preprocessor.transform(X)
        predictions = self.model.predict(X_transformed)
        
        return pd.DataFrame(predictions)
    
if __name__ == "__main__":
    with mlflow.start_run() as run:
        # Load object and train model
        CMP = CustomModelPredictor(
            var_features=var_features,
            target=target,
            model_params=model_params
        )
        
        # Read Data
        #
        #


        # Train the model
        signature = CMP.fit(data=train_data)

        # Log the model
        # conda_env = "conda.yaml"
        conda_env = {
            "name": "mlflow-env",
            "channels": ["defaults", "anaconda", "conda-forge"],
            "dependencies": [
                "python==3.7.0",
                "cloudpickle==1.6.0",
                "scikit-learn==0.22.1",
                "ortools==9.4.1874",
                "lightgbm==3.3.5",
            ],
        }
        artifacts = {
            "preprocessor": "/path/to/fitted_preprocessor.pkl",
            "estimator": "/path/to/fitted_model.pkl",
        }

        mlflow.pyfunc.log_model(
            artifact_path="model",
            artifacts=artifacts,
            python_model=CMP,
            conda_env=conda_env,
            signature=signature,
        )
