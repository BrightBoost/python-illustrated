class Pet:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def run(self):
        print(f"{self.name} is running.")

    def play(self):
        print(f"{self.name} is playing.")

# Override a method in the parent class
class Dog(Pet):
    def eat(self):
        print(f"{self.name} is eating from a marble bowl.")

# Also call the original method with super()
class Dog(Pet):
    def eat(self):
        super().eat()
        print("...from a marble bowl.")