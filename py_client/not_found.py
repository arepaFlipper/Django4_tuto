import requests

endpoint = "http://localhost:7890/api/products/290847129847219380/"

get_response = requests.get(endpoint)
print(get_response.json())
