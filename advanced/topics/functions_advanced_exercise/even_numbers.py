def get_even(numbers):
    return [int(x) for x in numbers.split() if int(x) % 2 == 0]


print(get_even(input()))
