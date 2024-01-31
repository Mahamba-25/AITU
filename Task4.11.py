import json

obj = {"name": "Jim", "age": 38, "city": "New York", "is_student": False}

data = json.dumps(obj, indent=2)
print("JSON Data:\n", data)

obj2 = json.loads(data)
print("\nObject Values:")
for key, value in obj2.items():
    print(f"{key}: {value}")
