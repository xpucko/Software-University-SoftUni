class Vet:
    animals = []
    space = 5

    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        result = 'Not enough space'
        if len(Vet.animals) < Vet.space:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            result = f'{animal_name} registered in the clinic'
        return result

    def unregister_animal(self, animal_name):
        result = f'{animal_name} not in the clinic'
        if animal_name in Vet.animals and animal_name in self.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            result = f'{animal_name} unregistered successfully'
        return result

    def info(self):
        return f'{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in clinic'
