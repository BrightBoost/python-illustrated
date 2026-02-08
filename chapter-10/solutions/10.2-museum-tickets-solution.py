def ticket_type():
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("That didn't work. Please enter a whole number.")
    if age < 0:
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
