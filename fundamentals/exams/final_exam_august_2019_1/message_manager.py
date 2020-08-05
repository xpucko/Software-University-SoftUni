capacity = int(input())
data = {}
while True:
    line = input().split('=')
    if line[0] == 'Statistics':
        print(f'Users count: {len(data)}')
        for k, v in sorted(data.items(), key=lambda x: (-x[1][1], x[0])):
            print(f'{k} - {sum(v)}')
        break
    elif line[0] == 'Add':
        if line[1] not in data:
            data[line[1]] = [int(line[2]), int(line[3])]
    elif line[0] == 'Message':
        if line[1] in data and line[2] in data:
            data[line[1]][0] += 1
            data[line[2]][1] += 1
            if data[line[1]][0] + data[line[1]][1] >= capacity:
                print(f'{line[1]} reached the capacity!')
                del data[line[1]]
            if data[line[2]][1] + data[line[2]][0] >= capacity:
                print(f'{line[2]} reached the capacity!')
                del data[line[2]]
    elif line[0] == 'Empty':
        if line[1] == 'All':
            data.clear()
        elif line[1] in data:
            del data[line[1]]