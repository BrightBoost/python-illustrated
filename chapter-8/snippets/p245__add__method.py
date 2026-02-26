class Cat:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return [self, other]

cat1 = Cat("Zia")
cat2 = Cat("Wiesje")
family = cat1 + cat2
print([cat.name for cat in family]) # ['Zia', 'Wiesje']




class Cat:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return  f"{self.name} + {other.name} = mischief"

cat1 = Cat("Zia")
cat2 = Cat("Wiesje")

print(cat1 + cat2)