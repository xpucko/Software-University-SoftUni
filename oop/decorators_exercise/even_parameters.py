def even_parameters(func):
    def wrapper(*args):
        for x in args:
            if not (isinstance(x, int) and x % 2 == 0):
                return 'Please use only even numbers!'
        return func(*args)

    return wrapper