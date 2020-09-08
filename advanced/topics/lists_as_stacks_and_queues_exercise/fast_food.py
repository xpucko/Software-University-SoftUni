from collections import deque

quantity = int(input())
orders = deque(int(x) for x in input().split())
print(max(orders))

for _ in range(len(orders)):
    current_order = orders.popleft()
    quantity -= current_order
    if quantity < 0:
        orders.appendleft(current_order)
        break

if not orders:
    print('Orders complete')
else:
    print('Orders left: ', end='')
    print(*orders)