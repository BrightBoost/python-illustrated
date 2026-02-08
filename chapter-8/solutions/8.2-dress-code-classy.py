class ClothingItem():
    def __init__(self, garment_type, size, color, fabric):
        self.garment_type = garment_type.lower() # all values set to lower case for consistency
        self.size = size.lower()
        self.color = color.lower()
        self.fabric = fabric.lower()
        # Setting initial attributes that are the same for all instances at first
        self.dirty = False
        self.times_worn = 0

    # A method to wear the item and set it to dirty after it has been worn.
    def wear(self):
        self.times_worn += 1
        print(f"Wearing {self.color} {self.garment_type}...")
        self.dirty = True

    # A method to check if an item needs washing and wash it if needed
    def wash(self):
        if not self.dirty:
            print(f"Hmm... I don't think this {self.color} {self.garment_type} needs washing")
        else:
            print(f"This {self.garment_type} is all clean again!")
            self.dirty = False # Not dirty anymore

    # A method to change the color of the garment
    def dye(self, new_color):
        self.color = new_color.lower()

    # To take care of clean prints:
    def __str__(self):
        return f"{self.color.capitalize()} {self.fabric} {self.garment_type}, size {self.size.capitalize()}"

	# Let's mix and match with __add__
    def __add__(self, other):
        combo = f"{self.color.capitalize()} {self.garment_type} + {other.color} {other.garment_type}"
        # Silly conditions for fashion verdicts
        if self.garment_type == other.garment_type:
            verdict = "I don't think you need two of those"
        elif self.color == other.color:
            verdict = "matchy-matchy"
        elif self.garment_type == "jeans" and other.garment_type == "shirt" or self.garment_type == "shirt" and other.garment_type == "jeans":
            verdict = "basic, but cute"
        elif self.color in ["pink", "red"] and other.color in ["pink", "red"]:
            verdict = "fashion disaster"
        else:
            verdict = "you do you"
        return f"{combo} = {verdict}"

    # Checking if two items are the same based on type, color, and size
    def __eq__(self, other):
        return self.garment_type == other.garment_type and self.color == other.color and self.size == other.size

# Creating a few items for our digital closet
shirt = ClothingItem("shirt", "M", "pink", "cotton")
jeans = ClothingItem("jeans", "M", "red", "linen")
jacket = ClothingItem("jacket", "L", "black", "denim")
copy_shirt = ClothingItem("shirt", "M", "pink", "cotton")

# Let's print a few
print(shirt)  	# Pink cotton shirt, size M
print(jacket) 	# Black denim jacket, size L

# Wearing and washing
print("\n-- Wardrobe in use --")
shirt.wear()
shirt.wear()
print(f"Worn {shirt.times_worn} times.")

shirt.wash()  	# Should wash
shirt.wash()  	# Should say it's already clean

# Dyeing
print("\n-- Getting crafty --")
jeans.dye("purple")
print(jeans)   # Purple linen trousers, size M

# Equality check
print("\n-- Are these the same item? --")
print(shirt == copy_shirt)   # True
print(shirt == jeans) 	# False

# Fashion verdicts
print("\n-- Fashion analysis --")
print(shirt + jeans) 
print(shirt + jacket)
print(shirt + copy_shirt) 
