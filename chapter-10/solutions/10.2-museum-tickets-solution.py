"""
A way to approach this:
1. Run the code and enter an age, oh dear, program crashes with TypeError
2. Read the traceback: "TypeError: '<' not supported between instances of 'str' and 'int'"
3. Identify the issue: input() returns a string, not an integer
4. The comparison 'age < 12' tries to compare string to int, which fails
5. Solution: Convert input to int with int()
6. Add try-except to handle cases where user enters non-numeric input
7. Bonus: Add validation for negative ages

Alternative debugging approach:
- Add print(type(age)) after input to see it's a string
- Set breakpoint before first if statement to inspect age variable type
"""

def ticket_type():
    # BREAKPOINT HERE (in original buggy code): Inspect type(age) to see it's a string
    # Why: Reveals that age is str, not int, explaining the TypeError
    while True:
        try:
            age = int(input("Enter your age: "))
            break # Only break if conversion succeeds
        except ValueError:
            print("That didn't work. Please enter a whole number.")
    if age < 0: # Bonus validation for negative ages
        print("That can't be right. Come back when you're born.")
    elif age < 12:
        print("You get in for free. Lucky you!")
    elif age < 18:
        print("You get a youth discount!")
    elif age < 65:
        print("That's a full-price ticket for you.")
    else:
        print("You get a senior discount!")

ticket_type()

# Bug was: input() returns string, can't compare string to int
# Fix: Convert to int with int(), wrap in try-except for non-numeric input
# Bonus: Added negative age validation