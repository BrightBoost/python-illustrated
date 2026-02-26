class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has-a Engine

    def drive(self):
        self.engine.start()
        print("Car is driving.")


car = Car()
car.drive()
