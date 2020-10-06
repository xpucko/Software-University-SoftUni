class Person:
    @staticmethod
    def sleep():
        return 'sleeping...'


class Employee:
    @staticmethod
    def get_fired():
        return 'fired...'


class Teacher(Person, Employee):
    @staticmethod
    def teach():
        return 'teaching...'
