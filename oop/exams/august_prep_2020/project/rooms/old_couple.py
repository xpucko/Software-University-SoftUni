from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    room_cost = 15
    appliances = [TV(), Fridge(), Stove(), TV(), Fridge(), Stove()]

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one + pension_two, 2)
        self.expenses = sum(a.get_monthly_expense() for a in self.appliances)
