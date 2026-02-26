class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

wiesje = Dog("Wiesje", 7, "brown")



class Dog:
    annoying = True # Class attribute

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color



class Dog:
    def __init__(self, name):
        self._name = name # Name marked private with an _

    # Getter method
    def get_name(self):
        return self._name

    # Setter method
    def set_name(self, new_name):
        if not new_name.strip() == "": # Checks for valid new_name
            self._name = new_name
        else:
            print("Invalid name!")



class Dog:
    def __init__(self, name):
        self._name = name
    
    # Getter method decorated with @ property
    @property
    def name(self):
        return self._name
    
    # Setter method decorated with @name.setter
    @name.setter
    def name(self, new_name):
        if not new_name.strip() == "":
            self._name = new_name
            print("Name changed!")
        else:
            print("Invalid name!")

wiesje = Dog("Wiesje")

print(wiesje.name) # Calling the getter method like a regular attribute

wiesje.name = "Teun" # Calling the setter method to change Wiesje's name



class Dog(): 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

wiesje = Dog("Wiesje", 7)
other_wiesje = Dog("Wiesje", 7)
chewie = Dog("Chewie", 10)

print(wiesje == other_wiesje) # Outputs True
print(wiesje == chewie) # Outputs False