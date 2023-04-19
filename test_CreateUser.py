import requests
import json


def test_create_new_user():
    # API URL
    url = "https://reqres.in/api/users"
    # Read Input Json File
    file = open("/Users/aliona/PycharmProjects/APIAutomation/create_post_training.json", "r")
    json_input = file.read()
    request_json = json.loads(json_input)
    # Make POST request with Json Input body
    response = requests.post(url, request_json)
    print(response.content)
    # Validating response Code
    assert response.status_code == 201
    # Fetch Header Response
    print(response.headers.get('Content_Length'))
