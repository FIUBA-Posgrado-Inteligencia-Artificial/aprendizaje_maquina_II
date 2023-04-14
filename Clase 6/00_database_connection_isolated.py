from sqlalchemy import create_engine
from sqlalchemy import text


#check this question to know the parameters https://stackoverflow.com/questions/3582552/what-is-the-format-for-the-postgresql-connection-string-url

port = '5342'
db_name = 'postgres'
user = 'postgres'
password = 'postgres'
ip = 'localhost'

#For remote dbs
#engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{ip}:{port}/{db_name}')

#For localhost there is no port
#engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{ip}/{db_name}')

id = 3
nombre = "nombre"
sql_insert = f"INSERT INTO public.tabla1 (id, nombre) VALUES ({id},'{nombre}')"
with engine.begin() as connection:
    x = connection.execute(text(sql_insert))

