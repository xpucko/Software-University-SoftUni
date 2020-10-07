from project.capacity_mixin import CapacityMixin


class ParkingMall(CapacityMixin):
    def __init__(self, parking_lots):
        self.parking_lots = parking_lots

    def check_availability(self):
        result = self.get_capacity(self.parking_lots, 1)
        if result == "Capacity reached!":
            return "There are no more parking lots!"
        self.parking_lots = result
        return f"Parking lots available: {self.parking_lots}"


