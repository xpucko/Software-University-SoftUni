from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        return f'Monthly consumption: {sum(room.expenses + room.room_cost for room in self.rooms):.2f}$.'

    def pay(self):
        for r in self.rooms:
            money_needed = r.room_cost + r.expenses
            current_budget = r.budget

            if current_budget < money_needed:
                self.rooms.remove(r)
                return f'{r.family_name} does not have enough budget and must leave the hotel.'

            r.budget -= money_needed
            return f'{r.family_name} paid {money_needed:.2f}$ and have {r.budget:.2f}$ left.'

    def status(self):
        result = f'Total population: {sum(x.members_count for x in self.rooms):.2f}\n'

        for r in self.rooms:
            result += f'{r.family_name} with {r.members_count} members. Budget: {r.budget}$, Expenses: {r.expenses}$\n'
            if r.children:
                for index, child in enumerate(r.children, start=1):
                    result += f'--- Child {index} monthly cost: {child.cost * 30:.2f}$\n'
            result += f'--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in r.appliances):.2f}$\n'

        return result
