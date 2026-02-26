def interactive_feeding():
    print("Welcome to the pet feeding station!")
    print("Type 'quit' when you're done feeding your pets.")
    
    while True:
        pet_name = input("What's your pet's name? ")
        
        if pet_name.lower() == "quit":
            print("All done feeding pets! Bye!")
            break
    
        species = input("What species is your pet? (e.g. cat, dog): ")
        food = input("What food do you want to give them? ")

        # A small decision based on the species input
        if species.lower() == "cat":
            print(pet_name, "arches their back and sniffs the", food)
        elif species.lower() == "dog":
            print(pet_name, "wags their tail at the sight of", food)
        else:
            print(pet_name, "looks curious about the", food)
        
        # Finally, we print a message about feeding
        print("Feeding", pet_name, "some delicious", food, "now!\n")

interactive_feeding()