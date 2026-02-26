def some_decorator(func):
    def wrapper():
        print("Something happens BEFORE the function is called.")
        func()
        print("Something happens AFTER the function is called.")
    return wrapper

def my_function():
    print("Hello from my_function")

my_function = some_decorator(my_function)
my_function()
