import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint) 
print("""🔏   \x1b[1;34;40m get_response:"""+get_response.text+"\x1b[0m") ## DELETEME
