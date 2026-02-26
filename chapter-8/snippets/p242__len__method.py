class ToyBox:
    def __init__(self, toys):
        self.toys = toys

    def __len__(self):
        return len(self.toys)

box = ToyBox(["Mouse", "Laser pointer", "Catnip banana"])
print(len(box)) 
