import json

obj = {"name": "Jim", "age": 38, "city": "New York"}
data = json.dumps(obj, indent=2)
print("JSON Data:", data)

with open("output.json", "w") as file: file.write(data)
