import requests
from getpass import getpass

def get_token():
    # password = getpass() 
    password = "qwerty" # this is bad I know don't look at me like that, I'm just too lazy to type password every single time
    auth_endpoint = "http://localhost:7890/api/auth/"
    auth_response = requests.post(auth_endpoint, json={'username': 'root', 'password': password})
    return auth_response.json()['token']
