import random

# Power Classes
class NineLives:
    def use(self):
        print("Revived.")

class SuperStrength:
    def use(self):
        print("Using super strength!")

class Invisibility:
    def use(self):
        print("Becoming invisible!")

class SuperBark:
    def use(self):
        print("Using a high pitched bark!")

class MezmerMeow:
    def use(self):
        print("Using a mezmerizing meow to confuse enemy!")

# Gadget Classes
class LaserWhiskers:
    def use(self):
        print("Using laser whiskers!")

class Shield:
    def use(self):
        print("Activating shield!")

class TeleportationCollar:
    def use(self):
        print("Using collar gadget for teleportation! Got away safely.")

class SpeedBoots:
    def use(self):
        print("Using speed boots to run fast as light!")

# Superhero Class
class Superhero:
    def __init__(self, name, powers, gadgets):
        self.name = name
        self.powers = powers  # List of power objects (composition)
        self.gadgets = gadgets  # List of gadget objects (composition)

    def fight_crime(self):
        # Randomly use a power or gadget
        all_tools = self.powers + self.gadgets
        random_tool = random.choice(all_tools)
        random_tool.use()  # Use the tool (power or gadget)

    def __str__(self):
        return f"{self.name} is ready to fight crime!"

# Create instances of powers and gadgets
strength = SuperStrength()
invisibility = Invisibility()
nine_lives = NineLives()
super_bark = SuperBark()
mezmer_meow = MezmerMeow()

laser_whiskers = LaserWhiskers()
shield = Shield()
collar = TeleportationCollar()
speed_boots = SpeedBoots()

# Create superheroes with lists powers and gadgets
zia = Superhero("Captain Code", [nine_lives, mezmer_meow], [laser_whiskers, shield, speed_boots])
wiesje = Superhero("Super Sausage", [super_bark, strength, invisibility], [shield, collar, speed_boots])

# Fight crime by using a random tool (power or gadget)
print(zia)  # Print superhero's info
zia.fight_crime()  # Use a random tool (power or gadget)

print(wiesje)
wiesje.fight_crime()
