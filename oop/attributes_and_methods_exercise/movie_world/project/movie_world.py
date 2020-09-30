class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def get_customer_by_id(self, customer_id):
        return [x for x in self.customers if x.id == customer_id][0]

    def get_dvd_by_id(self, dvd_id):
        return [x for x in self.dvds if x.id == dvd_id][0]

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.get_customer_by_id(customer_id)
        dvd = self.get_dvd_by_id(dvd_id)
        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                result = f'{customer.name} has already rented {dvd.name}'
            else:
                result = 'DVD is already rented'
        else:
            if customer.age < dvd.age_restriction:
                result = f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'
            else:
                dvd.is_rented = True
                customer.rented_dvds.append(dvd)
                result = f'{customer.name} has successfully rented {dvd.name}'

        return result

    def return_dvd(self, customer_id, dvd_id):
        customer = self.get_customer_by_id(customer_id)
        dvd = self.get_dvd_by_id(dvd_id)
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            result = f'{customer.name} has successfully returned {dvd.name}'
        else:
            result = f'{customer.name} does not have that DVD'

        return result

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += f'{customer.__repr__()}\n'
        for dvd in self.dvds:
            result += f'{dvd.__repr__()}\n'

        return result