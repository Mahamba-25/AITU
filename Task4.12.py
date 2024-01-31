import json

dictionary = {"name": "Jim", "age": 38, "city": "Mar Sara", "is_student": False}
data = json.dumps(dictionary, indent=4, sort_keys=True)
print(data)
