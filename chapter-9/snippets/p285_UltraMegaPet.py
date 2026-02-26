class Pet:
    def eat(self):
        print("Eating.")

class Wings:
    def fly(self):
        print("Flapping wings...")

class Fins:
    def swim(self):
        print("Splashing in the water...")

class LaserEyes:
    def shoot_lasers(self):
        print("Pew pew!")

class Sparkles:
    def sparkle(self):
        print("Magical sparkles everywhere!")

class UltraMegaPet(Pet):
    def __init__(self):
        self.wings = Wings()
        self.fins = Fins()
        self.lasers = LaserEyes()
        self.sparkles = Sparkles()