class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

cat1 = Cat("Zia", 1)
cat2 = Cat("Zia", 1)
cat3 = Cat("Garfield", 5)
print(cat1 == cat2)
print(cat1 == cat3)


# What will this output?
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return True

cat1 = Cat("Zia", 1)
cat2 = Cat("Zia", 1)
cat3 = Cat("Garfield", 5)
print(cat1 == cat2)
print(cat1 == cat3)