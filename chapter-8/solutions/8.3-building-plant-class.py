# Define a class Plant
class Plant():
    # A class attribute to keep track of the number of live plants
    count = 0

    # Define a constructor
    def __init__(self, name, size, desired_climate):
        self.name = name
        self.size = size
        self.desired_climate = desired_climate
        self.alive = True # Every plant starts out alive

        Plant.count += 1 # Updating the plant count

    def water(self):
        if not self.alive:
            print(f"There's no use... the {self.name.lower()} is no more.")
        else:
            print(f"Watering the {self.name.lower()}")

    def die(self):
        if not self.alive:
            print(f"The {self.name.lower()} is already dead.")
        else:
            print(f"The {self.name.lower()} withered away.")
            self.alive = False
            Plant.count -= 1 # decrease plant count when plant dies

    # The dunder method to fix weird print messages
    def __str__(self):
        return f"Name: {self.name} | Size: {self.size} | Preferred climate: {self.desired_climate} | Alive: {'yes' if self.alive else 'no'}"

# Test it!

plant_1 = Plant("Cactus", "Small", "Dry")
plant_2 = Plant("Monstera", "Large", "Tropical")
plant_3 = Plant("Fern", "Medium", "Tropical")

print(f"Plant count: {Plant.count}")

plant_1.water()
plant_1.die()

print(f"Plant count: {Plant.count}")

plant_1.water()

print(plant_2)
print(plant_1)
