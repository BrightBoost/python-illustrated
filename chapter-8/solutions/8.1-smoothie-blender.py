# Define a class Smoothie
class Smoothie:
    # constructor
    def __init__(self, ingredients):
        self._ingredients = [ingredient.lower() for ingredient in ingredients] # Puts all ingredients in lower case for consistency

    # @property decorator to deal with private attribute
    @property
    def ingredients(self):
        return self._ingredients

    # and a setter decorator
    @ingredients.setter
    def ingredients(self, new_ingredients):
        self._ingredients = new_ingredients

    # a method to add an ingredient
    def add_ingredient(self, ingredient):
        ingredient = ingredient.lower()
        self.ingredients.append(ingredient) # using append because ingredients is a list

    def describe(self): # If you used __str__, good job!
        print(f"A delicious smoothie with: {', '.join(self.ingredients)}") # a fancy way to create a beautiful stringified display of a list

    def __add__(self, other):
        # temporary empty list
        combined = []
        # Looping over all ingredients
        for ingredient in self.ingredients + other.ingredients:
            # only adding each ingredient once to the ingredients list
            if ingredient.lower() not in combined:
                combined.append(ingredient)
        return Smoothie(combined) # a new smoothie with combined ingredients

# Test it <3
drink1 = Smoothie(["strawberry"])
drink2 = Smoothie(["banana", "kale", "apple"])

drink1.add_ingredient("apple")

drink1.add_ingredient("apple")

drink3 = drink1 + drink2

drink3.describe()

