curl http://127.0.0.1:5000/invocations -H 'Content-Type: application/json' -d '{
  "dataframe_split": {
      "data": [[10, 10, 10,10], [0,0, 0, 0]]
  }
}'
