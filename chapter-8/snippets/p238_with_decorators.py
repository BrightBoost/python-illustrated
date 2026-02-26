def some_decorator(func):
    def wrapper():
        print("Something is happening BEFORE the function is called.")
        func()
        print("Something is happening AFTER the function is called.")
    return wrapper

@some_decorator
def my_function():
    print("Hello from my_function")

my_function()