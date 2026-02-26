class Cat:
    def __init__(self, name=None, age=None, color=None):
        self.name = name
        self.age = age
        self.color = color

def greet(self):
    print(f"{self.name} says: Meow!")

my_cat1 = Cat()
my_cat1.greet() # None says Meow!
my_cat2 = Cat("Zia", 1, "grey")
my_cat2.greet() # Zia says Meow!
