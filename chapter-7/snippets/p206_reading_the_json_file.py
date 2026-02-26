import json

with open("p206_pet_data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data["pet"])