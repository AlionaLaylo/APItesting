import requests
import json


# API URL
url = "https://reqres.in/api/users/2"

# Read Input Json File
file = open("/Users/aliona/PycharmProjects/APIAutomation/create_post_training.json", "r")
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with Json Input body
response = requests.put(url, request_json)
print(response.content)

# Validating response Code
assert response.status_code == 200

# Fetch Header Response
print(response.headers)
