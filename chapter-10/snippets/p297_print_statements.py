def add_pet(pets, name, age, species):
    pet = {"name": name, "age": age, "species": species, "fed": False}
    pets.append(pet)

def feed_pet(pets, name):
    for pet in pets:
        if pet['name'] == name:
            pet['fed'] = True
            print(f"{name} has been fed.")
my_pets = []

# This would be done with a user interface in real life
add_pet(my_pets, "Zia", 2, "cat")
add_pet(my_pets, "Wiesje", 7, "dog")
add_pet(my_pets, "Axel", 2, "axolotl")
feed_pet(my_pets, "wiesje")
# End of user interface simulation


# Adding a strategic print statement
def feed_pet(pets, name):
    for pet in pets:
        print(f"Checking pet: {pet['name']}") # This print statement is for debugging
        if pet['name'] == name:
            pet['fed'] = True
            print(f"{name} has been fed.")

# Adding another strategic print statement
def feed_pet(pets, name):
    for pet in pets:
        print(f"Checking pet: {pet['name']}") 
        if pet['name'] == name:
            print(f"In if block: {pet['name']}") # This one is new
            pet['fed'] = True
            print(f"{name} has been fed.")

# Still not seeing it, let's modify that first print statement
def feed_pet(pets, name):
    for pet in pets:
        print(f"Checking pet: {pet['name']} and {name}") # Now prints both name values
        if pet['name'] == name:
            print(f"In if block: {pet['name']}") 
            pet['fed'] = True
            print(f"{name} has been fed.")

# Fix:
feed_pet(my_pets, "Wiesje")

