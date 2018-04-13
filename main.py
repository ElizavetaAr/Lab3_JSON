import json

# to string
data = ['Test data', {'Structure': 'Any'}]
s = json.dumps(data)
print(s)

# from string
print(json.loads(s))
