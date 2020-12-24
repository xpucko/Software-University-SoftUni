def get_fibonacci(x):
    if x == 0 or x == 1:
        return 1

    return get_fibonacci(x - 1) + get_fibonacci(x - 2)


n = int(input())
print(get_fibonacci(n))
