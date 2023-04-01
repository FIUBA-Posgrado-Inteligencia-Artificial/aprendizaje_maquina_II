PGPASSWORD=apus psql -h 34.136.96.122 -d postgres -U postgres -c "\copy public.events TO 'data.csv' WITH (FORMAT csv,HEADER)"
python training_pipeline.py
rm data.csv
