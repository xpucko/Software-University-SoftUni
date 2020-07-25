def add_meal(guest, meal):
    if guest not in guests:
        guests[guest] = []
    if meal not in guests[guest]:
        guests[guest].append(meal)


def remove_meal(guest, meal):
    global count
    if guest in guests:
        if meal not in guests[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            guests[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")
            count += 1
    else:
        print(f'{guest} is not at the party.')


def print_data():
    for k, v in sorted(guests.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f'{k}: {", ".join(v)}')
    print(f'Unliked meals: {count}')


guests = {}
count = 0
while True:
    command = input().split('-')
    if command[0] == 'Stop':
        print_data()
        break
    elif command[0] == 'Like':
        add_meal(command[1], command[2])
    elif command[0] == 'Unlike':
        remove_meal(command[1], command[2])
