def even_odd(*args):
    return [x for x in args[:-1] if x % 2 == 0] if args[-1] == 'even' else [x for x in args[:-1] if x % 2 == 1]