class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print(f"{self.name} makes a sound!")
    # Other shared attributes and methods omitted to keep it short

class Cat(Pet):
    def speak(self):
        print(f"{self.name} says: Meow!")
    # Other cat specific details omitted
class Dog(Pet):
    def speak(self):
        print(f"{self.name} says: Woof!")
    # Other dog specific details omitted

class Rabbit(Pet):
    def speak(self):
        print(f"{self.name} says: Squeak!")
    # Other rabbit-specific details omitted


pets = [Cat("Zia", 1), Dog("Wiesje", 7), Rabbit("Ralph", 2)]
for pet in pets:
    pet.speak()
