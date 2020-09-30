class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription_info = [current for current in self.subscriptions if current.id == subscription_id][0]
        customer_info = [current for current in self.customers if current.id == subscription_id][0]
        trainer_info = [current for current in self.trainers if current.id == subscription_id][0]
        equipment_info = [current for current in self.equipment if current.id == subscription_id][0]
        plan_info = [current for current in self.plans if current.id == subscription_id][0]

        result = subscription_info.__repr__() + '\n' + \
            customer_info.__repr__() + '\n' + \
            trainer_info.__repr__() + '\n' + \
            equipment_info.__repr__() + '\n' + \
            plan_info.__repr__()

        return result
