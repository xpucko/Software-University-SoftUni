from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_cost = 30

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children: Child):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.children = [*children]
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.expenses = sum(a.get_monthly_expense() for a in self.appliances) + sum(c.cost * 30 for c in self.children)
