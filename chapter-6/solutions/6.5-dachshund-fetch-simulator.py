import random

def fetch(name, item):
    responses = [
        f"{name} fetched the {item}!",
        f"{name} ignored you.",
        f"{name} went after the {item}, but never brought it to you.",
        f"{name} got distracted!",
        f"{name} goes after the {item}, but halfway there, decides to take a nap."
    ]
    result = random.choice(responses)
    print(result)

fetch("Wiesje", "ball")