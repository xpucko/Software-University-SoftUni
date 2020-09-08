from collections import deque

bullet_price = int(input())
size_barrel = int(input())
bullets_list = [int(x) for x in input().split()]
locks_list = deque(int(x) for x in input().split())
intelligence_value = int(input())
counter = 0

while locks_list:
    counter += 1
    intelligence_value -= bullet_price
    bullet = bullets_list.pop()
    lock = locks_list.popleft()

    if lock < bullet:
        locks_list.appendleft(lock)
        print('Ping!')
    else:
        print('Bang!')

    if not bullets_list:
        break
    elif bullets_list and counter == size_barrel:
        counter = 0
        print('Reloading!')

if not locks_list:
    print(f'{len(bullets_list)} bullets left. Earned ${intelligence_value}')
else:
    print(f"Couldn't get through. Locks left: {len(locks_list)}")
