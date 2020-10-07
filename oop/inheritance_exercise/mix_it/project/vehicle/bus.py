from project.vehicle.vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, available_seats, ticket_price):
        Vehicle.__init__(self, available_seats)
        self.ticket_price = ticket_price
        self.tickets_sold = 0

    def get_ticket(self, tickets_count):
        result = self.get_capacity(self.available_seats, tickets_count)
        if result == "Capacity reached!":
            return result
        self.tickets_sold += tickets_count
        self.available_seats -= tickets_count
        return self.tickets_sold

    def get_total_profit(self):
        return self.ticket_price * self.tickets_sold
