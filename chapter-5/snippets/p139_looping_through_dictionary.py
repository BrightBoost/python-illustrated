cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna"
}

print("Cat attributes:")
for key in cat_attributes:
    print("-", key)

print("Cat attributes:")
for key in cat_attributes:
    print("-", key, ":", cat_attributes[key])

print("Cat attribute values:")
for value in cat_attributes.values():
    print("-", value)

print("Cat attributes and values:")
for key, value in cat_attributes.items():
    print(f"- {key}: {value}")