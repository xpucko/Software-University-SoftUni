def is_perfect_number(n):
    return "We have a perfect number!" if n == sum(x for x in range(1, n) if n % x == 0) else "It's not so perfect."


print(is_perfect_number(int(input())))
