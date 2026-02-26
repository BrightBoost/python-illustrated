class Pet:
    def eat(self):
        print("Nom nom nom")

class RoboPet(Pet):
    def charge(self):
        print("Charging...")

class RoboCat(RoboPet):
    def meow(self):
        print("Beep-meow!")