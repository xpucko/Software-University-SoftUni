from functools import wraps


def multiply(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * times

        return wrapper

    return decorator