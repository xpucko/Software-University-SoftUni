class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            result = 'Not enough budget'
        elif self.__animal_capacity == len(self.animals):
            result = 'Not enough space for animal'
        else:
            self.__budget -= price
            self.animals.append(animal)
            result = f'{animal.name} the {animal.__class__.__name__} added to the zoo'

        return result

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            result = f'{worker.name} the {worker.__class__.__name__} hired successfully'
        else:
            result = 'Not enough space for worker'

        return result

    def fire_worker(self, worker_name):
        worker = [x for x in self.workers if x.name == worker_name]
        if worker:
            self.workers.remove(worker[0])
            result = f'{worker_name} fired successfully'
        else:
            result = f'There is no {worker_name} in the zoo'

        return result

    def pay_workers(self):
        money_needed = sum([worker.salary for worker in self.workers])
        if money_needed <= self.__budget:
            self.__budget -= money_needed
            result = f'You payed your workers. They are happy. Budget left: {self.__budget}'
        else:
            result = f'You have no budget to pay your workers. They are unhappy'

        return result

    def tend_animals(self):
        money_needed = sum([animal.get_needs() for animal in self.animals])
        if money_needed <= self.__budget:
            self.__budget -= money_needed
            result = f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        else:
            result = f'You have no budget to tend the animals. They are unhappy.'

        return result

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [x for x in self.animals if x.__class__.__name__ == 'Lion']
        tigers = [x for x in self.animals if x.__class__.__name__ == 'Tiger']
        cheetahs = [x for x in self.animals if x.__class__.__name__ == 'Cheetah']

        result = f'You have {len(self.animals)} animals\n'
        result += f'----- {len(lions)} Lions:\n'
        result += '\n'.join([x.__repr__() for x in lions]) + '\n'
        result += f'----- {len(tigers)} Tigers:\n'
        result += '\n'.join([x.__repr__() for x in tigers]) + '\n'
        result += f'----- {len(cheetahs)} Cheetahs:\n'
        result += '\n'.join([x.__repr__() for x in cheetahs])

        return result

    def workers_status(self):
        keepers = [x for x in self.workers if x.__class__.__name__ == 'Keeper']
        caretakers = [x for x in self.workers if x.__class__.__name__ == 'Caretaker']
        vets = [x for x in self.workers if x.__class__.__name__ == 'Vet']

        result = f'You have {len(self.workers)} workers\n'
        result += f'----- {len(keepers)} Keepers:\n'
        result += '\n'.join([x.__repr__() for x in keepers]) + '\n'
        result += f'----- {len(caretakers)} Caretakers:\n'
        result += '\n'.join([x.__repr__() for x in caretakers]) + '\n'
        result += f'----- {len(vets)} Vets:\n'
        result += '\n'.join([x.__repr__() for x in vets])

        return result
