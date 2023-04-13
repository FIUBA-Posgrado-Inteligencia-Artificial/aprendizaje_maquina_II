curl http://127.0.0.1:5001/invocations -H 'Content-Type: application/json' -d '{
  "dataframe_split": {
      "data": [[10, 10, 10,10], [0,0, 0, 0]]
  }
}'


# For windows is 
# curl http://35.247.200.134:5001/invocations -H "Content-Type: application/json" -d "{  \"dataframe_split\": {      \"data\": [[-10,-10,50,3],[10, 10, 10,10], [0,0, 0, 0]]  }}"
