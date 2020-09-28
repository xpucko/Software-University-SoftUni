def get_sorted(numbers):
    return sorted(int(x) for x in numbers.split())


print(get_sorted(input()))