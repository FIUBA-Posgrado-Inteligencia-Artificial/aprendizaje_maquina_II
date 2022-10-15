from sqlalchemy import create_engine

#To see the result of the query the method is fetchall
#from sqlalchemy import create_engine

#check this question to know the parameters https://stackoverflow.com/questions/3582552/what-is-the-format-for-the-postgresql-connection-string-url
engine = create_engine('postgresql+psycopg2://postgres:?)T"L.GYq~FUdn]d@34.172.137.45:5432/postgres')
connection = engine.connect()
connection.execute(f"INSERT INTO events_data.predictions (user_id, predicted_revenue) VALUES ('{user_id}',{predicted_revenue})")
#return predicted_revenue
