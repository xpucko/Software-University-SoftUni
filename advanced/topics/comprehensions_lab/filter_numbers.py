def is_valid(number):
    results = [x for x in range(2, 11) if number % x == 0]
    return True if results else False


print([x for x in range(int(input()), int(input()) + 1) if is_valid(x)])