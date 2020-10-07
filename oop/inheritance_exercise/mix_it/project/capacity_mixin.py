class CapacityMixin:
    @staticmethod
    def get_capacity(capacity, amount):
        if amount > capacity:
            return "Capacity reached!"
        return capacity - amount
