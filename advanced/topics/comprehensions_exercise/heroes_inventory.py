names = input().split(', ')
heroes = {hero: {} for hero in names}

while True:
    tokens = input()
    if tokens == 'End':
        break
    name, item, cost = tokens.split('-')
    if name in heroes:
        if item not in heroes[name]:
            heroes[name][item] = int(cost)

[print(f'{hero} -> Items: {len(heroes[hero])}, Cost: {sum(heroes[hero].values())}') for hero in heroes]
