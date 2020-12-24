def get_factorial(x):
    if x == 0:
        return 1

    return x * get_factorial(x - 1)


n = int(input())
print(get_factorial(n))
