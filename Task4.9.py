import json

a = '{"name": "Jim", "age": 38, "city": "Mar Sara"}'
obj = json.loads(a)
print("Object:", obj)
print("Name:", obj['name'])
print("Age:", obj['age'])
print("City:", obj['city'])
