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

class Dog(Pet):
    pass

class Cat(Pet):
    pass

class Rabbit(Pet):
    pass

my_cat = Cat("Zia", 2.5, 1)
my_cat.eat() 


# Adding a breathe method for all pets:
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

    def breathe(self):
        print(f"{self.name} is breathing.")

my_dog = Dog("Wiesje", 2.5, 1)
my_dog.breathe()

# Adding methods to child classes
class Dog(Pet):
    def fetch(self):
        print(f"{self.name} is fetching the ball!")

class Cat(Pet):
    def climb(self):
        print(f"{self.name} is climbing the curtain. Again.")

class Rabbit(Pet):
    def hop(self):
        print(f"{self.name} is hopping around happily!")
