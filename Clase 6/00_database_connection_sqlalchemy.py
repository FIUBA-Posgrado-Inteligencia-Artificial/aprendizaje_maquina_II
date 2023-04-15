from sqlalchemy import create_engine
from sqlalchemy import text


#check this question to know the parameters https://stackoverflow.com/questions/3582552/what-is-the-format-for-the-postgresql-connection-string-url

port = '5342'
db_name = 'postgres'
user = 'postgres'
password = 'apu'
ip = '34.123.46.189'

#For remote dbs
#This one is not working 15th april 2023, but psygopg2 plain yes, let's user the other one until them
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{ip}:{port}/{db_name}')

#For localhost there is no port
#engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{ip}/{db_name}')

id = "d4899deb-2560-422e-8588-1066347a6604"
value = -1
sql_insert = f"INSERT INTO public.inference (id, value) VALUES ({id},value)"
with engine.begin() as connection:
    x = connection.execute(text(sql_insert))

