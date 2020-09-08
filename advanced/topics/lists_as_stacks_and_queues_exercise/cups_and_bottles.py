from collections import deque

cups = deque(map(int, input().split()))
bottles = deque(map(int, input().split()[::-1]))
wasted = 0

while bottles and cups:
    if bottles[0] >= cups[0]:
        wasted += bottles[0] - cups[0]
        cups.popleft()
    else:
        cups[0] -= bottles[0]
    bottles.popleft()

if bottles:
    print(f'Bottles: {" ".join(map(str, bottles))}')
if cups:
    print(f'Cups: {" ".join(map(str, cups))}')
print(f'Wasted litters of water: {wasted}')

# from collections import deque
#
# cups = deque(int(x) for x in input().split())
# bottles = [int(x) for x in input().split()]
# wasted = 0
#
# while bottles and cups:
#     cup = cups.popleft()
#     bottle = bottles.pop()
#     if cup <= bottle:
#         wasted += bottle - cup
#     else:
#         cups.appendleft(cup)
#         cups[0] -= bottle
#
# if bottles:
#     print('Bottles: ', end='')
#     print(*bottles)
# elif cups:
#     print(f'Cups: {" ".join(map(str, cups))}')
# print(f'Wasted litters of water: {wasted}')
