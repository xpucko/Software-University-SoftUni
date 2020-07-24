dragons = {}
for _ in range(int(input())):
    dragon_type, name, damage, health, armor = input().split()
    damage = 45 if damage == 'null' else damage
    health = 250 if health == 'null' else health
    armor = 10 if armor == 'null' else armor

    if dragon_type not in dragons:
        dragons[dragon_type] = {}
        dragons[dragon_type][name] = {}
    dragons[dragon_type][name] = [damage, health, armor]

for types, names in dragons.items():
    data, average_damage, average_health, average_armor = list(names.values()), 0, 0, 0
    for i in range(len(data)):
        average_damage += int(data[i][0]) / len(data)
        average_health += int(data[i][1]) / len(data)
        average_armor += int(data[i][2]) / len(data)
    print(f'{types}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})')
    names = sorted(names.items())
    for name, info in names:
        print(f'-{name} -> damage: {info[0]}, health: {info[1]}, armor: {info[2]}')