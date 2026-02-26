try:
    print("Great job so far,", name)
except:
    print("Oh no, something went wrong")

# Specify the exact error you want the except block to be triggered for
try:
    print("Great job so far,", name)
except NameError:
    print("Oh no, something went wrong")


# Add an else block to execute when try does not result in any errors
try:
    name = "Wiesje"
    print("Great job so far,", name)
except:
    print("Oh no, something went wrong")
else:
    print("Woohoo, all went well")


# Add a finally block if you need something to happen, error or not
try:
    name = "Wiesje"
    print("Great job so far,", name)
except:
    print("Oh no, something went wrong")
finally:
    print("You'll see this message, error or not")


# Handle FileNotFoundError gracefully:
try:
    with open("secret_plans.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
        print("No secret plans found. Perhaps they're locked away safely?")


# You can specify multiple excepts for different errors:
try:
    with open("secret_plans.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("No secret plans found. Perhaps they're locked away safely?")
except PermissionError:
    print("You do not have permission to access these secrets.")