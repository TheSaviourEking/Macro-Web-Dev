import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth"
password = getpass()


auth_response = requests.get(auth_endpoint, json={'username':"cfe", "password":password})
print (auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    endpoint = "https://localhost:8000/api/products"
    
    get_response = requests.get(endpoint)
    print(get_response.json())