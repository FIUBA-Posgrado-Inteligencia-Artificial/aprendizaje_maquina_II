"""
feature_engineering.py

COMPLETAR DOCSTRING

DESCRIPCIÓN:
AUTOR:
FECHA:
"""

# Imports

class FeatureEngineeringPipeline(object):

    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def read_data(self):
        """
        COMPLETAR DOCSTRING 
        
        """
            
        # COMPLETAR CON CÓDIGO
        
        return pandas_df

    
    def data_transformation(self, df):
        """
        COMPLETAR DOCSTRING
        
        """
        
        # COMPLETAR CON CÓDIGO
        
        return df_transformed

    def write_prepared_data(self, transformed_dataframe):
        """
        COMPLETAR DOCSTRING
        
        """
        
        # COMPLETAR CON CÓDIGO
        
        return None

    def run(self):
    
        df = self.read_data()
        df_transformed = self.data_transformation(df)
        self.write_prepared_data(df_transformed)

  
if __name__ == "__main__":
    FeatureEngineeringPipeline(input_path = 'Ruta/De/Donde/Voy/A/Leer/Mis/Datos',
                               output_path = 'Ruta/Donde/Voy/A/Escribir/Mi/Archivo').run()