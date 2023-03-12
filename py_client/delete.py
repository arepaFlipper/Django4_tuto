import requests

product_id = input("What is the id of the product you want to delete?\n")
try:
    product_id = int(product_id)
except:
    print("""💬   \x1b[1;31;40mdelete.py:7  error:""") ## DELETEME
    print(f'{product_id} is not a valid id') ## DELETEME
    print('\x1b[0m') ## DELETEME
    print(f'{product_id} is not a valid id')

if product_id:
    endpoint = f"http://localhost:7890/api/products/{product_id}/delete/"

    data = {"title":"Hello world I love my dactyl manuform keyboards", "price":129.99}
    get_response = requests.delete(endpoint, json=data)
    print("status_code: "+str(get_response.status_code)) ## DELETEME
