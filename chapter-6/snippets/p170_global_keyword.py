food = "kibble"

def feed_cat(): 
    global food
    food = "tuna"
    print("Feeding cat with", food)

feed_cat()
print(food)



# It's often better to pass variables as parameters and return updated values:
food = "kibble"
def feed_cat(food):
    food = "tuna"
    print("Feeding cat with", food)
    return food

food = feed_cat(food)
print(food)