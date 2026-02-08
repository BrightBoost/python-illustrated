remaining_treats = 200

def print_treats_left():
    print(f"You have {remaining_treats} treats left.")

def eat_treats(remaining_treats, eaten_treats):
    print(f"Ate {eaten_treats} treats.")
    remaining_treats = remaining_treats - eaten_treats

print_treats_left()
eat_treats(remaining_treats, 50)
print_treats_left()
