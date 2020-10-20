def vowel_filter(function):
    def wrapper():
        return [x for x in function() if x.lower() in {'a', 'e', 'o', 'u', 'i', 'y'}]

    return wrapper