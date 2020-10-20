class ValueCannotBeNegativeError(Exception):
    def __init__(self, value):
        message = f'Value {value} is negative.'
        super(ValueCannotBeNegativeError, self).__init__(message)


for _ in range(5):
    x = int(input())
    if x < 0:
        raise ValueCannotBeNegativeError(x)
