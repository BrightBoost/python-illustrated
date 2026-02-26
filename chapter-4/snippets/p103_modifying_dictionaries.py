cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna"
}

# Adding or updating entries
cat_attributes["hobby"] = "napping"

cat_attributes["age"] = 2

print("Updated attributes:", cat_attributes)

# Removing entries
del cat_attributes["favorite_food"]
print("After deletion:", cat_attributes)

del cat_attributes["breed"] # Will give an error


hobby = cat_attributes.pop("hobby")
print("Removed hobby:", hobby)
print("After popping 'hobby':", cat_attributes)


breed = cat_attributes.pop("breed") # Still gives the error

# Specify default value
breed = cat_attributes.pop("breed", "Not specified")
