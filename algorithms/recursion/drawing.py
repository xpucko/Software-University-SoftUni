def draw(x):
    if x == 0:
        return

    print('*' * x)
    draw(x - 1)
    print('#' * x)


n = int(input())
draw(n)
