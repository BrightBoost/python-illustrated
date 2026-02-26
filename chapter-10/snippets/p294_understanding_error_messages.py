def add_pet(pets, name, age, species):
    pet = {"name": name, "age": age, "species": species, "fed": False}
    pets.append(pet)

add_pet(my_pets, "Zia", 2, "cat")

# Read the traceback

# Fix:
def add_pet(pets, name, age, species):
    pet = {"name": name, "age": age, "species": species, "fed": False}
    pets.append(pet)

my_pets = []
add_pet(my_pets, "Zia", 2, "cat")
