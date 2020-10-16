def type_check(type_needed):
    def decorator(func):
        def wrapper(x):
            if isinstance(x, type_needed):
                return func(x)
            return f'Bad Type'

        return wrapper

    return decorator