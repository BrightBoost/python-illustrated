class Cat:
    def __init__(self, name, age):
        self._name = name # using underscore to hint it's 'private'
        self._age = age
    
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if len(new_name) > 0:
            self._name = new_name
        else:
            print("Invalid name!")