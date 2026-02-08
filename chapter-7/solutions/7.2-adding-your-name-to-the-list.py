# Ask the user to enter their name
name = input("What's your name? ").strip()

# Open attendance file
with open("attendance.txt", "a") as file:
    # Add name to the list
    file.write(f"{name}\n")

# print a success message
print(f"Welcome, {name}! You’ve been added to the list.")