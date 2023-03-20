import requests
from auth_token import get_token

endpoint = "http://localhost:7890/api/products/1/update/"

token = get_token()
headers = {'Authorization': f'Bearer {token}'}
data = {"title":"Another new product","body":"This is my new content", "price":3428930.23, "public": True}
get_response = requests.put(endpoint, json=data, headers=headers)
print(get_response.json())
