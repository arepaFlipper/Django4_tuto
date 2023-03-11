import requests

endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query":"Hello world"}) 
print("""🔏\x1b[1;34;40mget_response in regular text:"""+get_response.text+"\x1b[0m") ## DELETEME

print("""🚋\x1b[1;37;41mget_response.status_code:""") ## DELETEME
print(get_response.status_code) ## DELETEME
print('\x1b[0m') ## DELETEME
