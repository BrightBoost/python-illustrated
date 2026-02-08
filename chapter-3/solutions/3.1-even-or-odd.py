# Step 1: Store a number in a variable
number = 7 

# Step 2: Check if the number is even or odd using if/else
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")

# Bonus Challenge: Use ternary operator
result = "even" if number % 2 == 0 else "odd"
print(number, "is", result + ".")
