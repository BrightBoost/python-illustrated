remaining_treats = 200

def print_treats_left():
    print(f"You have {remaining_treats} treats left.")

def eat_treats(remaining, eaten_treats):
    print(f"Ate {eaten_treats} treats.")
    return remaining - eaten_treats  # Return the updated value

print_treats_left()
remaining_treats = eat_treats(remaining_treats, 50)  # Update the global variable
print_treats_left()

# Using the global keyword would work too:
remaining_treats = 200

def print_treats_left():
    print(f"You have {remaining_treats} treats left.")

def eat_treats(eaten_treats):
    print(f"Ate {eaten_treats} treats.")
    global remaining_treats
    remaining_treats -= eaten_treats  # Directly modify the global variable

print_treats_left()
eat_treats(50)
print_treats_left()
