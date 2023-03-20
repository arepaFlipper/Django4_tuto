import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:7890/api/?this_arg=this_value"

get_response = requests.post(endpoint, params={"product_id":123}, json={"title": "abc123", "content":"Hello world", "price":"this is an string"}) 
print(get_response.headers)



