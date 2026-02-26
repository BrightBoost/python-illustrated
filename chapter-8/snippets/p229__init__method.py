class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    def greet(self):
        print(f"{self.name} says: Meow!")

my_cat = Cat("Zia", 1, "grey")
my_cat.greet()

# Change attributes after setting them
my_cat = Cat("Zia", 1, "grey")
print(my_cat.age)
my_cat.age = 2
print(my_cat.age)

# Printing all attributes
my_cat = Cat("Zia", 1, "grey")
print(my_cat.name) # This line outputs "Zia"
print(my_cat.age) # This line outputs "1"
print(my_cat.color) # This line outputs "grey"
