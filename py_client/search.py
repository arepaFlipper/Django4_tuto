import requests
from auth_token import get_token

endpoint = "http://localhost:7890/api/search/?q=Another%20new%20product"
token = get_token()
headers = {
    "Authorization": f"Bearer {token}"
}
get_response = requests.get(endpoint, headers=headers)
data = get_response.json()
print(data)
# next_url = data['next']
# results = data['results']
