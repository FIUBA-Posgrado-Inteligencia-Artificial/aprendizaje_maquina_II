from metaflow import FlowSpec, step
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class ETLFlow(FlowSpec):

    @step
    def start(self):
        # MetaFlow necesita si o si un nodo de start y uno de end.
        print("🕐 Inicio de ETL con MetaFlow.")
        self.next(self.get_data)

    @step
    def get_data(self):
        """
        Carga los datos desde de la fuente
        """

        # Los mensajes se pasan como atributos de la clase.
        self.raw_data_path = "./data.csv"

        # Obtenemos el dataset
        print("📥 Descargando dataset de UCIML...")
        dataset = fetch_ucirepo(id=45).data.original

        print("🧹 Normalizando columna 'num'...")
        dataset.loc[dataset["num"] > 0, "num"] = 1

        dataset.to_csv(self.raw_data_path, index=False)

        # Pasamos al siguiente nodo
        self.next(self.make_dummies)

    @step
    def make_dummies(self):
        """
        Convierte a las variables en Dummies
        """
        print(f"📂 Leyendo archivo: {self.raw_data_path}")
        df = pd.read_csv(self.raw_data_path)

        print("🧼 Eliminando duplicados y nulos...")
        df.drop_duplicates(inplace=True, ignore_index=True)
        df.dropna(inplace=True, ignore_index=True)

        print("🔄 Convertiendo columnas categóricas a enteros...")
        for col in ["cp", "restecg", "slope", "ca", "thal"]:
            df[col] = df[col].astype(int)
        
        print("🏷️ Generando variables dummy...")
        df = pd.get_dummies(df, columns=["cp", "restecg", "slope", "ca", "thal"], drop_first=True)
        
        self.clean_data_path = "./data_clean_dummies.csv"
        df.to_csv(self.clean_data_path, index=False)
        self.shape = df.shape
        self.next(self.split_data)

    @step
    def split_data(self):
        """
        Genera el dataset y obtiene set de testeo y evaluación
        """
        df = pd.read_csv(self.clean_data_path)
        assert df.shape == self.shape, "⚠️ La forma del dataset no coincide con lo esperado."
        
        print("🔀 Separando dataset en entrenamiento y prueba...")
        X = df.drop(columns=["num"])
        y = df["num"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)
        
        self.X_train_path = "./X_train.csv"
        self.X_test_path = "./X_test.csv"
        self.y_train_path = "./y_train.csv"
        self.y_test_path = "./y_test.csv"
        
        X_train.to_csv(self.X_train_path, index=False)
        X_test.to_csv(self.X_test_path, index=False)
        y_train.to_csv(self.y_train_path, index=False)
        y_test.to_csv(self.y_test_path, index=False)
        print("✅ Datos de entrenamiento y prueba guardados.")

        self.next(self.normalize)

    @step
    def normalize(self):
        """
        Estandarizamos los datos
        """

        print("🔢 Leyendo datos para normalizar...")
        X_train = pd.read_csv(self.X_train_path)
        X_test = pd.read_csv(self.X_test_path)

        print("📏 Estandarizando variables numéricas...")
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        self.X_train_norm_path = "./X_train_norm.csv"
        self.X_test_norm_path = "./X_test_norm.csv"

        pd.DataFrame(X_train_scaled, columns=X_train.columns).to_csv(self.X_train_norm_path, index=False)
        pd.DataFrame(X_test_scaled, columns=X_test.columns).to_csv(self.X_test_norm_path, index=False)
        print("✅ Datos normalizados y guardados.")

        self.next(self.read_train, self.read_test)

    @step
    def read_train(self):
        """
        Leemos los datos de entrenamiento
        """
        X_train = pd.read_csv(self.X_train_norm_path)
        y_train = pd.read_csv(self.y_train_path)
        print(f"📚 Datos de entrenamiento: X={X_train.shape}, y={y_train.shape}")
        self.next(self.join)

    @step
    def read_test(self):
        """
        Leemos los datos de testeo
        """
        X_test = pd.read_csv(self.X_test_norm_path)
        y_test = pd.read_csv(self.y_test_path)
        print(f"🧪 Datos de testeo: X={X_test.shape}, y={y_test.shape}")
        self.next(self.join)

    @step
    def join(self, _):
        # Este paso es necesario para unir la bifurcacion, porque a MetaFlow no le gusta llegar al end si unirse
        self.next(self.end)

    @step
    def end(self):
        print("✅ Proceso ETL completo con MetaFlow.")

if __name__ == "__main__":
    ETLFlow()
