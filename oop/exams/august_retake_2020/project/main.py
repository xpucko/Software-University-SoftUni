from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren

from project.people.child import Child

from project.everland import Everland

everland = Everland()


def test_one():
    young_couple = YoungCouple("Johnsons", 150, 205)

    child_one = Child(5, 1, 2, 1)
    child_two = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child_one, child_two)

    everland.add_room(young_couple)
    everland.add_room(young_couple_with_children)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()

"""
Monthly consumtions: 1136.00$.
Johnsons paid 242.00$ and have 355.00$ left.
Peterson paid 894.00$ and have 1120.00$ left.
Total population: 6
Johnsons with 2 members. Budget: 113.00$, Expenses: 222.00$
--- Appliances monthly cost: 222.00$
Peterson with 4 members. Budget: 226.00$, Expenses: 864.00$
--- Child 1 monthly cost: 270.00$
--- Child 2 monthly cost: 150.00$
--- Appliances monthly cost: 444.00$
"""