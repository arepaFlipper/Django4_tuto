import requests

endpoint = "http://localhost:7890/api/products/"

data = { "title":"This field is done"}
get_response = requests.post(endpoint, json=data)
print("""📗 \x1b[1;32;40mget_response.status_code:""") ## DELETEME
print(get_response.status_code) ## DELETEME
print('\x1b[0m') ## DELETEME
print(get_response.json())
