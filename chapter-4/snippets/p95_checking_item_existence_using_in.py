cat_toys = ["feather", "mouse toy", "ball", "laser pointer", "scratching post"]
item_exists = "laser pointer" in cat_toys



if "laser pointer" in cat_toys:
    print("Time to play with the laser pointer!")
else:
    print("No laser pointer found.")



cat_toys = ["feather", "mouse toy", "ball", "laser pointer", "scratching post", "cardboard box"]

if "cardboard box" in cat_toys:
    print("Oh no, she's throwing away my box!")
    cat_toys.remove("cardboard box")
else:
    print("No box to throw away.")