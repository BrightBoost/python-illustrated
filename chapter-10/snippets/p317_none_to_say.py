def log_call(func):
    def wrapper(self):
        print(f"{self.name} is about to speak...")
        func(self)
    return wrapper

class Animal:
    def __init__(self, name):
        self.name = name

    @log_call
    def speak(self):
        return "..."

class Dog(Animal):
    @log_call
    def speak(self):
        return "Woof!"

class Cat(Animal):
    @log_call
    def speak(self):
        return "Meow!"

dog = Dog("Cliff")
cat = Cat("Muchu")

print(dog.speak())
print(cat.speak())