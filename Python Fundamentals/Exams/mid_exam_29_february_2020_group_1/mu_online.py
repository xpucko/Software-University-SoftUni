rooms = input().split('|')
health = 100
bitcoins = 0
is_dead = False

for i in range(len(rooms)):
    room = rooms[i].split()
    command = room[0]
    number = int(room[1])
    if command == 'potion':
        if health + number > 100:
            print(f'You healed for {100 - health} hp.')
            health = 100
        else:
            health += number
            print(f'You healed for {number} hp.')
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        health -= number
        if health <= 0:
            print(f'You died! Killed by {command}.')
            is_dead = True
            print(f'Best room: {i + 1}')
            break
        print(f'You slayed {command}.')

if not is_dead:
    print("You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')