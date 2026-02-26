cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna"
}
cat_name = cat_attributes["name"]
print("My name is", cat_name)



cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna"
}

breed = cat_attributes["breed"] # Python raises a KeyError



# Using get() method to prevent KeyError
cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna"
}

breed = cat_attributes.get("breed")
print("Breed:", breed)



# Specify default value
breed = cat_attributes.get("breed", "Unknown")
print("Breed:", breed)