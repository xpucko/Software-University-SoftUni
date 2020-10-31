data = {}
for _ in range(int(input())):
    line = input().split('<->')
    data[line[0]] = [int(line[1]), [0]]

while True:
    line = input().split(': ')
    if line[0] == 'Exhibition':
        break

    command, tokens = line[0], line[1]
    if command == 'Rate':
        plant, rating = tokens.split(' - ')
        if plant in data:
            data[plant][1].append(int(rating))
        else:
            print('error')
    elif command == 'Update':
        plant, rarity = tokens.split(' - ')
        if plant in data:
            data[plant][0] = int(rarity)
        else:
            print('error')
    elif command == 'Reset':
        plant = line[1]
        if plant in data:
            data[plant][1] = [0]
        else:
            print('error')

print(f'Plants for the exhibition:')
for k, v in sorted(data.items(), key=lambda x: (x[1][0], sum(x[1][1]) / len(x[1][1])), reverse=True):
    if sum(v[1]) == 0:
        print(f'- {k}; Rarity: {v[0]}; Rating: 0.00')
    else:
        print(f'- {k}; Rarity: {v[0]}; Rating: {sum(v[1]) / (len(v[1]) - 1):.2f}')
