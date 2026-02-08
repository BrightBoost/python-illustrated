def checkout():
    """Asks the user for the number of items and their prices, then prints the total cost."""
    num_items = int(input("How many items are you buying? "))
    total = 0


    for i in range(1, num_items + 1):
        price = float(input(f"Enter price of item {i}: "))
        total += price


    print(f"Total: ${total}")

checkout()


