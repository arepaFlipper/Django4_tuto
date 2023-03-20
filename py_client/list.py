import requests
from auth_token import get_token

endpoint = "http://localhost:7890/api/products/?limit=3&offset=8"
token = get_token()
headers = {
    "Authorization": f"Bearer {token}"
}
get_response = requests.get(endpoint, headers=headers)
print(get_response.json())
data = get_response.json()
next_url = data['next']
results = data['results']
