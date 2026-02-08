# Step 1: Store the dachshund's name
name = "Wiesje"

# Step 2: Store the weight in kilograms
weight_kg = 2.5  

# Step 3: Convert weight to pounds
weight_lbs = weight_kg * 2.2

# Step 4: Classify the dachshund's size
if weight_lbs < 12:
    classification = "Kaninchen"
elif 12 <= weight_lbs <= 16:
    classification = "Miniature"
else:
    classification = "Standard"

# Step 5: Print the result
print("With a weight of", weight_kg, "kgs,", weight_lbs, "lbs, dachshund", name, "is classified as:", classification + ".")


