def get_primes(numbers):
    for x in numbers:
        if x >= 2:
            for n in range(2, x):
                if x % n == 0:
                    break
            else:
                yield x