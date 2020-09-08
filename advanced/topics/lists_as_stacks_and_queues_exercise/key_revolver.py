from collections import deque

bullet_price = int(input())
gun_size = int(input())
bullets = list(map(int, input().split()))[::-1]
locks = deque(map(int, input().split()))
value = int(input())
shots = 0

for i in range(len(bullets)):
    if bullets[i] <= locks[0]:
        locks.popleft()
        print('Bang!')
    else:
        print('Ping!')

    shots += 1
    value -= bullet_price

    if shots == gun_size and i != len(bullets) - 1:
        shots = 0
        print('Reloading!')

    if not locks:
        print(f'{len(bullets) - i - 1} bullets left. Earned ${value}')
        break

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
