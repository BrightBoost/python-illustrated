"""
A way to approach this:
1. Run the code, it prints the log messages but then prints "None" for both animals
2. Expected output: 
    - "Cliff is about to speak..."
    - "Woof!"
    But getting:
    - "Cliff is about to speak..."
    - "None"
3. Add print statement in wrapper to see what func(self) returns:
    result = func(self)
    print(f"DEBUG: func returned {result}")
4. Realize: The decorator calls func(self) but doesn't return the result
5. The speak() method returns a string, but the wrapper doesn't pass it through
6. Fix: Add 'return' before func(self) in the wrapper

Alternative debugging approach:
- Set breakpoint in the wrapper function
- Step through and watch the return value of func(self)
- Notice that the wrapper has no return statement
- The decorated function's return value is lost
"""

def log_call(func):
    def wrapper(self):
        print(f"{self.name} is about to speak...")
        # BREAKPOINT HERE: Step through to see func(self) returns a value
        # Why: Reveals that we're calling func but not returning its result
        # The value is lost because wrapper doesn't return anything
        return func(self) # Fixed: Added 'return' to pass through the result
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

# Bug was: Decorator's wrapper function called func(self) but didn't return the result
# Fix: Added 'return' statement in wrapper to pass through the function's return value
# Expected output:
# Cliff is about to speak...
# Woof!
# Muchu is about to speak...
# Meow!