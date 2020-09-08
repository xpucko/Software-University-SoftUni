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
