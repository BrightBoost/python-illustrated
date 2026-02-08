import random

def sorting_hat():
    houses = ("Slytherin", "Gryffindor", "Ravenclaw", "Hufflepuff")
    house = random.choice(houses)
    print(f"You belong in... {house}")

sorting_hat()

# bonus challenge
import random
import time

def sorting_hat():
    houses = ("Slytherin", "Gryffindor", "Ravenclaw", "Hufflepuff")
    print("The sorting hat is thinking...")
    time.sleep(2)
    house = random.choice(houses)
    print(f"You belong in {house}!")

sorting_hat()