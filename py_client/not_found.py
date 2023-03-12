import requests

endpoint = "http://localhost:7890/api/products/290847129847219380/"

get_response = requests.get(endpoint)
print("status_code: "+str(get_response.status_code)) ## DELETEME
print("""📗 \x1b[1;36;40mget_response.status_code:""") ## DELETEME
print(get_response.json())
print('\x1b[0m') ## DELETEME
