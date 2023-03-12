import requests

endpoint = "http://localhost:7890/api/products/1/update/"

data = {"title":"Hello world I love my dactyl manuform keyboards", "price":129.99}
get_response = requests.put(endpoint, json=data)
print("status_code: "+str(get_response.status_code)) ## DELETEME
print("""📗 \x1b[1;36;40mget_response.status_code:""") ## DELETEME
print(get_response.json())
print('\x1b[0m') ## DELETEME
