import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)

# Display Response Content
print(f'Response code: {response.status_code}')
print(response.content)
print(response.json())
print(response.text)
print(response.headers['Content-Type'])
print(response.headers['Cache-Control'])

assert response.headers['Cache-Control'] == 'max-age=14400'
assert response.status_code == 200

# assert rb == response.json() # check with TM

# Parse response to Json format

json_response = json.loads(response.text)

print(json_response)
# Fetch value using Json Path
pages = jsonpath.jsonpath(json_response, 'total_pages')
