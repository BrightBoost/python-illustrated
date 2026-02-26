class Pet:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def run(self):
        print(f"{self.name} is running.")

    def play(self):
        print(f"{self.name} is playing.")

class Cat(Pet):
    def __init__(self, name, age, weight, number_of_lives_left):
        super().__init__(name, age, weight)
        self.number_of_lives_left = number_of_lives_left

    def climb(self):
        print(f"{self.name} is climbing the curtain. Again.")
