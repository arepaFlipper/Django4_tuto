import requests
from auth_token import get_token

endpoint = "http://localhost:7890/api/v2/"
token = get_token()
print("""❔   \x1b[1;33;40mlist.py:6    token:""") ## DELETEME
print(token) ## DELETEME
print('\x1b[0m') ## DELETEME
headers = {
    "Authorization": f"Bearer {token}"
}
get_response = requests.get(endpoint, headers=headers)
print("status_code: "+str(get_response.status_code)) ## DELETEME
print("""📗 \x1b[1;34;40mget_response.status_code:""") ## DELETEME
print(get_response.json())
print('\x1b[0m') ## DELETEME

endpoint2 = [*get_response.json().values()][0]
get_response = requests.get(endpoint2, headers=headers)
print("""🧪   \x1b[1;36;40mapi_v2.py:23 get_response.json():""") ## DELETEME
print(get_response.json()) ## DELETEME
print('\x1b[0m') ## DELETEME
endpoint2 = endpoint2 + '1/'
get_response = requests.get(endpoint2, headers=headers)
print("""😤   \x1b[1;30;43mapi_v2.py:25 get_response.json():""") ## DELETEME
print(get_response.json()) ## DELETEME
print('\x1b[0m') ## DELETEME
