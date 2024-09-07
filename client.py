#reads data.json as a string and passes it the the OpenAI API, which sends back a response

import requests
import json

# open JSON file
with open('data.json', 'r') as f:
    # parse JSON data
    data = json.load(f)

response=requests.post(
    "http://localhost:8000/chain/invoke",
    json={'input':{'text': data}}
)

str = response.json()['output']

split = str.splitlines()

print(split)

print(split[0])

