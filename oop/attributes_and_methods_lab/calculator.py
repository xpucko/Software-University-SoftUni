class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for arg in args:
            result *= arg

        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for arg in args[1:]:
            result /= arg

        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for arg in args[1:]:
            result -= arg

        return result
