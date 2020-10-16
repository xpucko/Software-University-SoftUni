def cache(func):
    def wrapper(num):
        wrapper.log[num] = func(num)
        return func(num)

    wrapper.log = {}

    return wrapper