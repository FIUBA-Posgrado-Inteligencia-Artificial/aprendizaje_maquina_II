"""
predict.py

COMPLETAR DOCSTRING

DESCRIPCIÓN:
AUTOR:
FECHA:
"""

# Imports

class MakePredictionPipeline(object):
    
    def __init__(self, input_path, output_path, model_path: str = None):
        self.input_path = input_path
        self.output_path = output_path
        self.model_path = model_path
                
                
    def load_data(self):
        """
        COMPLETAR DOCSTRING
        """

        return data

    def load_model(self):
        """
        COMPLETAR DOCSTRING
        """    
        self.model = load_model(self.model_path) # Esta función es genérica, utilizar la función correcta de la biblioteca correspondiente
        
        return None


    def make_predictions(self, data):
        """
        COMPLETAR DOCSTRING
        """
   
        new_data = self.model.predict(data)

        return new_data


    def write_predictions(self, predicted_data):
        """
        COMPLETAR DOCSTRING
        """

        return None


    def run(self):

        data = self.load_data()
        self.load_model()
        df_preds = self.make_predictions(data)
        self.write_predictions(df_preds)


if __name__ == "__main__":
    
    
    pipeline = MakePredictionPipeline(input_path = 'Ruta/De/Donde/Voy/A/Leer/Mis/Datos',
                                      output_path = 'Ruta/Donde/Voy/A/Escribir/Mis/Datos',
                                      model_path = 'Ruta/De/Donde/Voy/A/Leer/Mi/Modelo')
    pipeline.run()  