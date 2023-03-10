import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, data={"query":"Hello world"}) 
print("""🔏\x1b[1;34;40mget_response in regular text:"""+get_response.text+"\x1b[0m") ## DELETEME
print("""⛺\x1b[1;36;40mget_response in JSON:""") ## DELETEME
print(get_response.json()) ## DELETEME
print('\x1b[0m') ## DELETEME
