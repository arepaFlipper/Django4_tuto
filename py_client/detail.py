import requests
from auth_token import get_token

endpoint = "http://localhost:7890/api/products/24/"
token = get_token()
headers = {'Authorization': f'Bearer {token}'}

get_response = requests.get(endpoint, headers=headers)
print("status_code: "+str(get_response.status_code)) ## DELETEME
print("""📗 \x1b[1;36;40mget_response.status_code:""") ## DELETEME
print(get_response.json())
print('\x1b[0m') ## DELETEME
