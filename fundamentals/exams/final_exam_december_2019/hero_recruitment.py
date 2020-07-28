heroes = {}
while True:
    line = input().split()
    if line[0] == 'End':
        print('Heroes:')
        for name, spells in sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0])):
            print(f'== {name}: {", ".join(spells)}')
        break
    hero = line[1]
    if line[0] == 'Enroll':
        if hero not in heroes:
            heroes[hero] = []
        else:
            print(f"{hero} is already enrolled.")
    elif line[0] == 'Learn':
        spell = line[2]
        if hero not in heroes:
            print(f"{hero} doesn't exist.")
        else:
            print(f'{hero} has already learnt {spell}.') if spell in heroes[hero] else heroes[hero].append(spell)
    elif line[0] == 'Unlearn':
        spell = line[2]
        if hero not in heroes:
            print(f"{hero} doesn't exist.")
        else:
            heroes[hero].remove(spell) if spell in heroes[hero] else print(f"{hero} doesn't know {spell}.")
