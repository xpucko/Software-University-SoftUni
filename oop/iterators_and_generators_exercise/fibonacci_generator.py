def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y