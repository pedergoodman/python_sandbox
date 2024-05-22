# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
# pares dictionary into JSON
# parse JSON into a dictionary

import json

#sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

user = json.loads(userJSON)

print(user)
print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)
print(type(user))

print(f"User JSON: {userJSON}")
print(f"User dictionary: {user}")
print(f"Car JSON: {carJSON}")
print(f"Car dictionary: {car}")

