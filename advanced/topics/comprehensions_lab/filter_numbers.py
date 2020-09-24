print([x for x in range(int(input()), int(input()) + 1) if any([x % n == 0 for n in range(2, 11)])])
