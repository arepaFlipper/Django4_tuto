import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:7890/api/"

print("""🖼️   \x1b[1;37;40mbasic.py:7   requests.__version__:""") ## DELETEME
print(requests.__version__) ## DELETEME
print('\x1b[0m') ## DELETEME
get_response = requests.get(endpoint, params={"abc":123}, json={"query":"Hello world"}) 
print("""🔏\x1b[1;34;40mget_response in regular text:"""+get_response.text+"\x1b[0m") ## DELETEME

print("""⛺\x1b[1;36;40mget_response in JSON:""") ## DELETEME
print(get_response.json()) ## DELETEME
print('\x1b[0m') ## DELETEME

print("""📗 \x1b[1;32;40mget_response.status_code:""") ## DELETEME
print(get_response.status_code) ## DELETEME
print('\x1b[0m') ## DELETEME

