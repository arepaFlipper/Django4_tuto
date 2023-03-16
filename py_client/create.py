import requests
from auth_token import get_token

endpoint = "http://localhost:7890/api/products/"
token = get_token()
headers = {'Authorization': f'Bearer {token}'}

data = {"title":"Product new post", "content":"if you can", "price": "32.99"}
get_response = requests.post (endpoint, json=data, headers=headers)
print("status_code: "+str(get_response.status_code)) ## DELETEME
print("""📗 \x1b[1;32;40mget_response.status_code:""") ## DELETEME
print(get_response.json())
print('\x1b[0m') ## DELETEME
