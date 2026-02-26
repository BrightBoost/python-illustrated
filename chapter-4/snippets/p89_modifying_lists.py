# Adding items
cat_toys = ["feather", "ball", "laser pointer", "scratching post"]
cat_toys.append("cardboard box")
print("Updated toys:", cat_toys)

cat_toys.insert(1, "mouse toy")
print("After inserting at index 1:", cat_toys)

# Removing items
cat_toys = ["feather", "mouse toy", "ball", "laser pointer", "scratching post", "cardboard box"]
cat_toys.remove("ball")
print("After removing 'ball':", cat_toys)

cat_toys.pop(2)
print("After popping index 2:", cat_toys)

# Changing items
cat_toys = ["feather", "mouse toy", "ball", "laser pointer", "scratching post", "cardboard box"]
cat_toys[0] = "cat wand"
print("After changing:", cat_toys)