class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def ride(self):
        print(f"{self.make} {self.model} is riding")

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, has_sunroof, is_electric):
        super().__init__(make, model, year)
        self.has_sunroof = has_sunroof
        self.is_electric = is_electric

    def __str__(self):
        return f"{'Electric ' if self.is_electric else ''}{super().__str__()}, with{'out' if not self.has_sunroof else ''} sunroof"

class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def can_carry(self, weight):
        return self.payload_capacity >= weight 

    def __str__(self):
        return f"{super().__str__()}, Payload Capacity: {self.payload_capacity} tons"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_type):
        super().__init__(make, model, year)
        self.engine_type = engine_type

    def do_wheelie(self):
        print("Popping a wheelie.")

    def rev_engine(self):
        print("Vroom vroom")

    def __str__(self):
        return f"{super().__str__()}, Engine: {self.engine_type}"

my_car = Car("Fiat", "Multipla", 2002, False, False)
my_truck = Truck("CAT", "735", 2021, 32)
my_motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2017, "twin engine")

my_list = [my_car, my_truck, my_motorcycle]

for vehicle in my_list:
    print(vehicle)
    vehicle.ride()
