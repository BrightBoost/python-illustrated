# Infinite while loops
i = 0
while i < 5:
    print(i)
    # Missing increment



# Modifying a list while looping over it
toys = ["ball", "hedgehog"]

for item in toys:
    toys.append("new toy")
    print(toys)



# What will this print?
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)


# Removing items while looping can skip elements
numbers = [1, 2, 2, 3, 4, 4, 5]
for num in numbers:
    if num == 2:
        numbers.remove(num)
print(numbers)



# Fix: loop over a copy
numbers = [1, 2, 2, 3, 4, 4, 5]
for num in numbers[:]:
    if num == 2:
        numbers.remove(num)

print(numbers)



# Off-by-one errors, make sure you understand step size and that range is exclusive
for i in range(0, 4, 2):
    print(i)