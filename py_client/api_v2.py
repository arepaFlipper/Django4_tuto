import requests
from auth_token import get_token

endpoint = "http://localhost:7890/api/v2/"
token = get_token()
headers = {
    "Authorization": f"Bearer {token}"
}
get_response = requests.get(endpoint, headers=headers)
print(get_response.json())

endpoint2 = [*get_response.json().values()][0]
get_response = requests.get(endpoint2, headers=headers)
endpoint2 = endpoint2 + '1/'
get_response = requests.get(endpoint2, headers=headers)
