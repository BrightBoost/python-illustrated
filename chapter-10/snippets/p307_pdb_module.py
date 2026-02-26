def add_pet(pets, name, age, species):
    pet = {"name": name, "age": age, "species": species, "fed": False}
    pets.append(pet)
    
def feed_pet(pets, name):
    breakpoint()
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
