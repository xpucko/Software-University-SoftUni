def logged(func):
    def wrapper(*args):
        return f'you called {func.__name__}{args}\nit returned {func(*args)}'

    return wrapper