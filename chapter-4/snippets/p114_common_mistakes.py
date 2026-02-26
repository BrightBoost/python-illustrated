# IndexError with lists and tuples
some_numbers = [1, 2, 3]
print(some_numbers[3]) # Giving IndexError: list index out of range


index = 3
if index < len(some_numbers):
    print(some_numbers[index])
else:
    print("Index out of range.")


# KeyError with dictionaries
friends_ages = {"Zia": 1, "Wiesje": 7, "Muchu": 0}
print(friends_ages["Szara"]) # KeyError: 'Szara'

key = "Szara"
if key in friends_ages:
    print(friends_ages[key])
else:
    print("Key not found.")

key = "Szara"
value = friends_ages.get(key, "Key not found.")
print(value)