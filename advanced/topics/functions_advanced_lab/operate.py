def operate(operator, *args):
    result = None
    if operator == '+':
        result = sum(args)
    elif operator == '-':
        result = 0
        for n in args:
            result -= n
    elif operator == '*':
        result = 1
        for i in args:
            result *= i
    elif operator == '/':
        result = 1
        for i in args:
            result /= i

    return result
