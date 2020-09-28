def func_executor(*args):
    return [x[0](*x[1]) for x in args]
