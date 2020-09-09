guests_list = set(input() for _ in range(int(input())))
guests_arrived = set()

while True:
    guest = input()
    if guest == 'END':
        break
    guests_arrived.add(guest)

result = sorted(guests_list.difference(guests_arrived))
print(len(result))
[print(x) for x in result if x[0].isdigit()]
[print(x) for x in result if not x[0].isdigit()]
