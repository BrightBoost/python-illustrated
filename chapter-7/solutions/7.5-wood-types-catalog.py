import json

# Define a function that displays each wood type
def load_woods():
    try:
        with open("wood_types.json", "r") as file:
            woods = json.load(file)
            return woods
    except FileNotFoundError:
        print("Hmm... Couldn't find the wood encyclopedia.")

def display_woods():
    woods = load_woods()
    for wood in woods:
        # create a string with use cases
        uses = ""
        for i in range(len(wood["uses"])):
            uses += wood["uses"][i]
            if i < len(wood["uses"]) - 1:
                uses += ", "

        print(f"Name: {wood["name"]}")
        print(f"Hardness: {wood["hardness"]}")
        print(f"Color: {wood["color"]}")
        print(f"Uses: {uses}")
        print("\n")

display_woods()

def add_wood(name, hardness, color, uses):
    new_wood = {
        "name": name,
        "hardness": hardness,
        "color": color,
        "uses": uses
    }

    woods = load_woods()
    woods.append(new_wood)

    with open("wood_types.json", "w") as file:
        json.dump(woods, file)

# add_wood("Dark Oak", 8, "dark brown", ["flooring", "furniture", "cabinets", "architectural trim"])

def filter_wood(use):
    woods = load_woods()
    print(f"Woods commonly used for {use}:")
    for wood in woods:
        if use in wood["uses"]:
            print(wood["name"])

filter_wood("furniture")

