import requests

endpoint="http://localhost:8000/api/"
res=requests.get(endpoint,params={"key":"value"},json={"query":"helloworld"})

print(res.json())

