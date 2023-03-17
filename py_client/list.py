import requests
from auth_token import get_token

endpoint = "http://localhost:7890/api/products/"
token = get_token()
print("""❔   \x1b[1;33;40mlist.py:6    token:""") ## DELETEME
print(token) ## DELETEME
print('\x1b[0m') ## DELETEME
headers = {
    "Authorization": f"Bearer {token}"
}
get_response = requests.get(endpoint, headers=headers)
print("status_code: "+str(get_response.status_code)) ## DELETEME
print("""📗 \x1b[1;36;40mget_response.status_code:""") ## DELETEME
print(get_response.json())
print('\x1b[0m') ## DELETEME
data = get_response.json()
next_url = data['next']
print("""▫️   \x1b[1;33;40mlist.py:20   next_url:""") ## DELETEME
print(next_url) ## DELETEME
print('\x1b[0m') ## DELETEME
results = data['results']
print("""🍺   \x1b[1;34;40mlist.py:20   results:""") ## DELETEME
print(results) ## DELETEME
print('\x1b[0m') ## DELETEME
