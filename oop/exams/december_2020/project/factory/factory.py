from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    @abstractmethod
    def add_ingredient(self, ingredient_type: str, quantity: int):
        ...

    @abstractmethod
    def remove_ingredient(self, ingredient_type: str, quantity: int):
        ...

    def can_add(self, value: int):
        return value <= self.capacity
