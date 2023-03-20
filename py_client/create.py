import requests
from auth_token import get_token

endpoint = "http://localhost:7890/api/articles/"
token = get_token()
headers = {'Authorization': f'Bearer {token}'}

data = {"title":"Blog Articles are Simple", "body":"This is a new blog article", "public":True}
get_response = requests.post (endpoint, json=data, headers=headers)
print(get_response.json())
