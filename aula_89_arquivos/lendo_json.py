import json
with open('abc.json', 'r') as file:
    pessoas2_json = file.read()
    pessoas2_json = json.loads(pessoas2_json)

