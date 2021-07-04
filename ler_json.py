import json

with open('abc.json', 'r') as file:
    d1_jason = file.read()
    d1_jason = json.loads(d1_jason)
    print(d1_jason)
