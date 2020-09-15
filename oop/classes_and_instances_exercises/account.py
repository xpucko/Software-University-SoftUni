class Account:
    def __init__(self, id: int, name: str, balance=0):
        self.id = id
        self.name = name
        if balance:
            self.balance = balance
        else:
            self.balance = 0

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        result = 'Amount exceeded balance'

        if amount <= self.balance:
            self.balance -= amount
            result = self.balance

        return result

    def info(self):
        return f'User {self.name} with account {self.id} has {self.balance} balance'
