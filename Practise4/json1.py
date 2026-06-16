import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(type(y))

# ----

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# ----

data = {"name": "Alex", "age": 20}
with open("data.json", "w") as f:
    json.dump(data, f)

# ---
with open("data.json", "r") as f:
    data = json.load(f)

print(data)
print(type(data))