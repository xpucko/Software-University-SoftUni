from collections import deque


def solve():
    names = deque()
    while True:
        name = input()
        if name == 'End':
            print(f'{len(names)} people remaining.')
            break
        elif name == 'Paid':
            while names:
                print(names.popleft())
        else:
            names.append(name)


solve()
