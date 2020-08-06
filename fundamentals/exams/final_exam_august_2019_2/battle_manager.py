data = {}
while True:
    line = input().split(':')
    if line[0] == 'Results':
        print(f'People count: {len(data)}')
        for k, v in sorted(data.items(), key=lambda x: (-x[1][0], x[0])):
            print(f'{k} - {v[0]} - {v[1]}')
        break
    elif line[0] == 'Add':
        person, health, energy = line[1], int(line[2]), int(line[3])
        if person not in data:
            data[person] = [health, energy]
        else:
            data[person][0] += health
    elif line[0] == 'Attack':
        attacker, defender, damage = line[1], line[2], int(line[3])
        if attacker in data and defender in data:
            data[defender][0] -= damage
            if data[defender][0] <= 0:
                del data[defender]
                print(f'{defender} was disqualified!')
            data[attacker][1] -= 1
            if data[attacker][1] <= 0:
                del data[attacker]
                print(f'{attacker} was disqualified!')
    elif line[0] == 'Delete':
        if line[1] == 'All':
            data.clear()
        elif line[1] in data:
            del data[line[1]]