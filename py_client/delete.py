import requests

product_id = input("What is the id of the product you want to delete?\n")
try:
    product_id = int(product_id)
except:
    print(f'{product_id} is not a valid id')

if product_id:
    endpoint = f"http://localhost:7890/api/products/{product_id}/delete/"

    data = {"title":"Hello world I love my dactyl manuform keyboards", "price":129.99}
    get_response = requests.delete(endpoint, json=data)
