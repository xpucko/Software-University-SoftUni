class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self):
        return f'{self.name} {self.surname}'


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(name=None, people=(self.people + other.people))

    def __getitem__(self, item):
        if isinstance(item, int):
            return f'Person {item}: {self.people[item]}'

    def __repr__(self):
        return f'Group {self.name} with members {", ".join([h.__repr__() for h in self.people])}'