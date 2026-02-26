import random

roll = random.randint(1,6)
print("Dice roll:", roll)


val = random.random()
print("A random float between 0 and 1:", val)


pets = ["Zia", "Wiesje", "Axolotl King"]
chosen_pet = random.choice(pets)
print("Your random pet is:", chosen_pet)


toys = ["ball", "laser pointer", "feather wand"]
random.shuffle(toys)
print("Shuffled toys:", toys)


sample_toys = random.sample(toys, 2)
print("Randomly chosen toys:", sample_toys)