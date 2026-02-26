class Pet:
    def eat(self):
        print("Eating.")

class FlyingPet(Pet):
    def fly(self):
        print("Flapping wings...")

class SwimmingFlyingPet(FlyingPet):
    def swim(self):
        print("Splashing in the water...")

class LaserSwimmingFlyingPet(SwimmingFlyingPet):
    def shoot_lasers(self):
        print("Pew pew!")

class InvisibleLaserSwimmingFlyingPet(LaserSwimmingFlyingPet):
    def turn_invisible(self):
        print("Now you see me, now you don't.")

class UnicornInvisibleLaserSwimmingFlyingPet(InvisibleLaserSwimmingFlyingPet):
    def sparkle(self):
        print("Magical sparkles everywhere!")

pet = UnicornInvisibleLaserSwimmingFlyingPet()
pet.fly()
pet.swim()
pet.shoot_lasers()
pet.turn_invisible()
pet.sparkle()

