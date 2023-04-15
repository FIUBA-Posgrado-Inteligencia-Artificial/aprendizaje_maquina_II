import psycopg2

port = '5342'
db_name = 'postgres'
user = 'postgres'
password = 'apu'
ip = '34.123.46.189'

conn_string = f"host='{ip}' dbname='{db_name}' user='{user}' password='{password}'"
with psycopg2.connect(conn_string) as conn:
    cursor = conn.cursor()
    cursor.execute("""insert into public.inference("value") values(-1)""")
    conn.commit() # <- We MUST commit to reflect the inserted data
    cursor.close()
