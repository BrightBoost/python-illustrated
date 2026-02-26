def get_pet_info():
    pet_name = input("What's your pet's name? ")
    
    if pet_name.lower() == "quit":
        return None
    
    species = input("What species is your pet? (e.g. cat, dog): ")
    food = input("What food do you want to give them? ")
    return (pet_name, species, food)

def feed_pet(pet_name, species, food):
    if species.lower() == "cat":
        print(pet_name, "arches their back and sniffs the", food)
    elif species.lower() == "dog":
        print(pet_name, "wags their tail excitedly at the sight of", food)
    else:
        print(pet_name, "looks curious about the", food)
    
    print("Feeding", pet_name, "some delicious", food, "now!\n")

def interactive_feeding():
    print("Welcome to the pet feeding station!")
    print("Type 'quit' when you're done feeding your pets.")
    
    while True:
        pet_data = get_pet_info()
        
        if pet_data is None: # user typed 'quit' for the pet's name
            print("All done feeding pets! Bye!")
            break
    
        pet_name, species, food = pet_data
        feed_pet(pet_name, species, food)

# Call the main function to start the feeding loop
interactive_feeding()