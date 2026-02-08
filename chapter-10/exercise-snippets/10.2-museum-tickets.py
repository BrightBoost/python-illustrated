def ticket_type():
    age = input("Enter your age: ")

    if age < 12:
        print("You get in for free. Lucky you!")
    elif age < 18:
        print("You get a youth discount!")
    elif age < 65:
        print("That's a full-price ticket for you.")
    else:
        print("You get a senior discount!")

ticket_type()

