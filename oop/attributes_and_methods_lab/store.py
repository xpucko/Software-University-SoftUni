class Store:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def from_size(cls, name, type, size):
        return cls(name, type, size // 2)

    def add_item(self, item_name):
        if self.capacity == 0:
            result = 'Not enough capacity in the store'
        else:
            if item_name not in self.items:
                self.items[item_name] = 0

            self.items[item_name] += 1
            self.capacity -= 1
            result = f'{item_name} added to the store'

        return result

    def remove_item(self, item_name, amount):
        if item_name not in self.items or self.items[item_name] < amount:
            result = f'Cannot remove {amount} {item_name}'
        else:
            self.items[item_name] -= amount
            self.capacity += amount
            result = f'{amount} {item_name} removed from the store'

        return result

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)
print(first_store)
print(second_store)
print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))
