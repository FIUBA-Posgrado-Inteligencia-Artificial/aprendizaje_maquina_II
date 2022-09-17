PGPASSWORD=XXXXXX psql -h XXXXX -d postgres -U postgres -c "\copy data.table1 TO 'data.csv' WITH (FORMAT csv)"
python training_pipeline.py
rm data.csv