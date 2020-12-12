from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        valid = ['white chocolate', 'dark chocolate', 'milk chocolate', 'sugar']

        if ingredient_type not in valid:
            raise TypeError(f'Ingredient of type {ingredient_type} not allowed in ChocolateFactory')

        if not self.can_add(quantity):
            raise ValueError('Not enough space in factory')

        if ingredient_type not in self.ingredients:
            self.ingredients[ingredient_type] = 0
        self.ingredients[ingredient_type] += quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients:
            raise KeyError('No such product in the factory')

        if self.ingredients[ingredient_type] < quantity:
            raise ValueError('Ingredient quantity cannot be less than zero')

        self.ingredients[ingredient_type] -= quantity

    def add_recipe(self, recipe_name: str, recipe: dict):
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        if recipe_name not in self.recipes:
            raise TypeError('No such recipe')

        for product in self.recipes[recipe_name]:
            self.remove_ingredient(product, 1)

        if recipe_name not in self.products:
            self.products[recipe_name] = 0
        self.products[recipe_name] += 1
