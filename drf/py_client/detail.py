import requests

endpoint = "http://localhost:8000/api/products/1"

get_response = requests.get(endpoint, json = {"title":"Hello World?"})

print(get_response.text)
print(get_response.status_code)