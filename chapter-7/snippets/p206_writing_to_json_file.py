import json
data = {
    "pet": "Zia",
    "toys": ["feather wand", "ball", "laser pointer"],
    "weight": 2.2
}

with open("p206_pet_data.json", "w") as file:
    json.dump(data, file)