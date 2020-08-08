heroes = {}
for _ in range(int(input())):
    data = input().split()
    hero_name, hp, mp = data[0], int(data[1]), int(data[2])
    hp = 100 if hp > 100 else hp
    mp = 200 if mp > 200 else mp
    heroes[hero_name] = [hp, mp]

while True:
    line = input().split(' - ')
    if line[0] == 'End':
        for k, v in sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])):
            print(f'{k}\n  HP: {v[0]}\n  MP: {v[1]}')
        break

    hero = line[1]
    amount = int(line[2])
    if line[0] == 'Recharge':
        if heroes[hero][1] + amount > 200:
            print(f'{hero} recharged for {200 - heroes[hero][1]} MP!')
            heroes[hero][1] = 200
        else:
            heroes[hero][1] += amount
            print(f'{hero} recharged for {amount} MP!')
    elif line[0] == 'Heal':
        if heroes[hero][0] + amount > 100:
            print(f'{hero} healed for {100 - heroes[hero][0]} HP!')
            heroes[hero][0] = 100
        else:
            heroes[hero][0] += amount
            print(f'{hero} healed for {amount} HP!')
    elif line[0] == 'CastSpell':
        if heroes[hero][1] < amount:
            print(f'{hero} does not have enough MP to cast {line[3]}!')
        else:
            heroes[hero][1] -= amount
            print(f'{hero} has successfully cast {line[3]} and now has {heroes[hero][1]} MP!')
    elif line[0] == 'TakeDamage':
        if heroes[hero][0] <= amount:
            del heroes[hero]
            print(f'{hero} has been killed by {line[3]}!')
        else:
            heroes[hero][0] -= amount
            print(f'{hero} was hit for {amount} HP by {line[3]} and now has {heroes[hero][0]} HP left!')