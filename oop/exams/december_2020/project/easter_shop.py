from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    def __init__(self, name, chocolate_factory: ChocolateFactory, egg_factory: EggFactory, paint_factory: PaintFactory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = {}

    def add_chocolate_ingredient(self, type: str, quantity: int):
        self.chocolate_factory.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type: str, quantity: int):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type: str, quantity: int):
        self.paint_factory.add_ingredient(type, quantity)

    def make_chocolate(self, recipe: str):
        self.chocolate_factory.make_chocolate(recipe)

        if recipe not in self.storage:
            self.storage[recipe] = 0
        self.storage[recipe] += 1

    def paint_egg(self, color: str, egg_type: str):
        if egg_type not in self.egg_factory.products or color not in self.paint_factory.products:
            raise ValueError('Invalid commands')

        key = f'{color} {egg_type}'
        if key not in self.storage:
            self.storage[key] = 0
        self.storage[key] += 1

        self.egg_factory.remove_ingredient(egg_type, 1)
        self.paint_factory.remove_ingredient(color, 1)

    def __repr__(self):
        result = f'Shop name: {self.name}\n'
        result += 'Shop Storage:\n'
        for name, quantity in self.storage.items():
            result += f'{name}: {quantity}\n'

        return result
