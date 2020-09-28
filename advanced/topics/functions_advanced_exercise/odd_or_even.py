def solve(command, numbers_str):
    length = len(numbers_str.split())
    numbers = [int(x) for x in numbers_str.split()]

    if command == 'Odd':
        result = sum([x for x in numbers if x % 2 == 1]) * length
    else:
        result = sum([x for x in numbers if x % 2 == 0]) * length

    return result


print(solve(input(), input()))
