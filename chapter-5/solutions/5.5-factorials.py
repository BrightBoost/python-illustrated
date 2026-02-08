number = 5
factorial = 1

if number < 0:
    print("Factorials are only defined for non-negative integers.")
else:
    for i in range(number, 0, -1): # there are more ways to do this
        factorial *= i
    print(f"{number}! = {factorial}")


