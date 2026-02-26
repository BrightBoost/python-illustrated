class Cat:
    def __init__(self, name):
        self._name = name # _ so it is marked as 'private'

    @property
    def name(self):
        return self._name


my_cat = Cat("Zia")
print(my_cat.name) # prints "Zia"


class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 0:
            self._name = new_name
        else:
            print("Invalid name!")


my_cat = Cat("Zia")
print(my_cat.name) # This calls the getter and prints "Zia"
my_cat.name = "Garfield" # This calls the setter
print(my_cat.name) # This calls the getter and prints "Garfield"
my_cat.name = "" # Prints "Invalid name!" and keeps the old one