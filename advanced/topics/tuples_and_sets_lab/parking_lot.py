parking = set()
for _ in range(int(input())):
    direction, car = input().split(', ')
    if direction == 'IN':
        parking.add(car)
    else:
        parking.remove(car)

if not parking:
    print('Parking Lot is Empty')
else:
    [print(x) for x in parking]
