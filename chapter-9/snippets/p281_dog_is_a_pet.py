class Pet:
    def __init__(self, name):
        self.name = name
class Dog(Pet):  # Dog is-a Pet
    def bark(self):
        print(f"{self.name} says: Woof!")

dog = Dog("Wiesje")
print(dog.name)  # Inherited from Pet
dog.bark()       # Dog-specific behavior
