import streamlit as st
import pandas as pd
import numpy as np
import joblib

from sqlalchemy import create_engine


def connect_to_db():
    """
    Función para conectarse a la base de datos PostgreSQL.
    Returns:
        Objeto Engine de SQLAlchemy para la conexión a la base de datos.
    """

    # Advertencia: Evite codificar en duro las credenciales de la base de datos. Considere usar variables de entorno o
    # archivos de configuración en su lugar.
    db_dict = {
        "host": "postgres",
        "database": "salaries",
        "user": "postgres",
        "port": "5432",
        "password": "postgres"
    }
    engine = create_engine(f'postgresql://{db_dict["user"]}:{db_dict["password"]}@{db_dict["host"]}:{db_dict["port"]}/{db_dict["database"]}')
    return engine


def fetch_names(engine):
    """
    Función para obtener los nombres de los empleados desde la base de datos.
    Args:
        engine: Objeto Engine de SQLAlchemy para la conexión a la base de datos.
    Returns:
        Lista de nombres de empleados.
    """
    query = "SELECT first_name, last_name FROM salary_data;"
    df = pd.read_sql(query, engine)
    df["name"] = df["first_name"] + " " + df["last_name"]

    return df["name"].sort_values().to_list()


def fetch_employee_data(engine, name):
    """
    Función para obtener los datos de un empleado desde la base de datos según su nombre.
    Args:
        engine: Objeto Engine de SQLAlchemy para la conexión a la base de datos.
        name: Nombre del empleado.
    Returns:
        DataFrame que contiene los datos del empleado.
    """
    name_splitted = name.split()
    query = f"""
            SELECT *
            FROM salary_data
            WHERE first_name = '{name_splitted[0]}' AND last_name = '{name_splitted[-1]}'
            """
    df = pd.read_sql(query, engine)

    return df


def load_model():
    """
    Función para cargar el artefacto del modelo
    Returns:
        Modelo de aprendizaje automático cargado.
    """
    return joblib.load('./salary_model.pkl')


def format_currency(value):
    """
    Función para formatear un valor numérico como moneda.
    Args:
        value: Valor numérico a formatear.
    Returns:
        Cadena de moneda formateada.
    """
    # Formatea el valor como cadena con separadores de miles y dos decimales
    formatted_value = "{:,.2f}".format(value)
    # Agrega el símbolo de la moneda al principio
    formatted_currency = "$" + formatted_value
    return formatted_currency


def currency_to_float(currency_string):
    """
    Función para convertir una cadena de moneda formateada a float.
    Args:
        currency_string: Cadena de moneda formateada.
    Returns:
        Valor float.
    """
    # Elimina el símbolo de la moneda y los separadores de miles
    numeric_string = currency_string.replace('$', '').replace(',', '')
    # Convierte la cadena a float
    float_value = float(numeric_string)
    return float_value


def main():
    st.title("RRHH Tool - Analizador de incremento de sueldos")

    # Conecta a la base de datos
    engine = connect_to_db()

    # Carga el artefacto del modelo
    model = load_model()

    # Verifica si la conexión es exitosa
    if engine is not None:
        # Obtiene datos de la base de datos
        names_list = fetch_names(engine)

        # Con los nombres, arma un desplegable
        name = st.selectbox("Nombre del empleado", names_list)

        # Con el nombre seleccionado, se recupera de la base de datos el resto de los datos
        df = fetch_employee_data(engine, name)

        # Si los datos no están vacíos
        if not df.empty:
            # Se muestran los datos
            st.subheader("Dato del empleado")

            # Obtenemos los datos del puesto en que trabaja el empleado y que seniority tiene. Esto es para el modelo
            position = df['job'].values[0]
            seniority = df['experience'].values[0]

            # Esta lista es para seleccionar inputs del modelo
            seniority_list = ["Semi-senior", "Senior"]
            if seniority == "Semi-senior":
                seniority_list = ["Senior"]

            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f":red[Nombre:] {df['first_name'].values[0]}")
                st.markdown(f":red[Posición:] {position}")
                st.markdown(f":red[Email:] {df['email'].values[0]}")
                st.markdown(f":rainbow[Salario anual actual:] {df['salary'].values[0]}")

                # Si la persona tiene un seniority máximo, no se muestra al modelo ni el selector de nuevo seniority.
                if seniority != "Senior":
                    new_seniority = st.selectbox("Nuevo seniority:", seniority_list)

            with col2:
                st.markdown(f":red[Apellido:] {df['last_name'].values[0]}")
                st.markdown(f":red[Seniority:] {seniority}")
                st.markdown(f":red[Teléfono:] {df['phone'].values[0]}")

            # Si la persona tiene un seniority menor a Senior, se observa que puesto tiene y que seniority nuevo se
            # seleccionó, con ello armamos el input del modelo.
            if seniority != "Senior":
                input_model = np.array([0, 0, 0, 0])
                if position == "Consultant":
                    input_model[0] = 1
                if position == "Engineer":
                    input_model[1] = 1
                if new_seniority == "Semi-Senior":
                    input_model[2] = 1
                if new_seniority == "Senior":
                    input_model[3] = 1

                # Obtenemos el nuevo salario del modelo
                new_salary = model.predict(input_model.reshape(1, -1))[0]
                new_salary = np.round(new_salary, -2)

                # Si el salario anterior es mayor al nuevo, se ofrece por defecto mejorarlo en 3000 dólares
                old_salary = currency_to_float(df['salary'].values[0])
                if old_salary > new_salary:
                    new_salary = old_salary + 3000

                # Se muestra el resultado del modelo
                st.markdown(f":rainbow[Nuevo salario anual:] {format_currency(new_salary)}")

        engine.dispose()
    else:
        st.error("Fallo la conexión con la base de datos.")

if __name__ == "__main__":
    main()
