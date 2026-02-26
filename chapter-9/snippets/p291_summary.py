# Pet and Engine classes are omitted, these are the snippets in the summary

class Cat(Pet):
    pass

class Cat(Pet):
    def __init__(self, name, age, weight, color):
        super().__init__(name, age, weight)
        self.color = color

class Car:
    def __init__(self):
        self.engine = Engine() # Car has-a Engine