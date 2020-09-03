class Flower:
    is_happy = False

    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements

    def water(self, quantity):
        self.is_happy = quantity >= self.water_requirements

    def status(self):
        result = f"{self.name} is not happy"

        if self.is_happy:
            result = f"{self.name} is happy"

        return result
