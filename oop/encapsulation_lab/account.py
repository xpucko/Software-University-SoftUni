class Account:
    def __init__(self, id, balance, pin):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        result = 'Wrong pin'
        if pin == self.__pin:
            result = self.__id

        return result

    def change_pin(self, old_pin, new_pin):
        result = 'Wrong pin'
        if old_pin == self.__pin:
            self.__pin = new_pin
            result = 'Pin changed'

        return result
