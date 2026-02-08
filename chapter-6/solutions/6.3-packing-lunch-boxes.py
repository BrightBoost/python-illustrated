def pack_lunchbox(**items):
    print("You packed your lunchbox:")

    # Print packed items
    for category, item in items.items():
        print(f"{category}: {item}")

    # Print reminder for snack if necessary
    if not "snack" in items:
        print("Better pack a snack!")

# Example usage:
pack_lunchbox(main="sandwich", snack="cookie", drink="juice")
print("")
pack_lunchbox(main="salad")
print("")
pack_lunchbox(main="pasta", snack="chips", fruit="apple", drink="water")