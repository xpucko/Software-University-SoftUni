def even_numbers(function):
    def wrapper(numbers):
        return [x for x in function(numbers) if x % 2 == 0]

    return wrapper