users = {}
while True:
    line = input().split('->')
    if line[0] == 'Statistics':
        print(f'Users count: {len(users)}')
        for user, message in sorted(users.items(), key=lambda x: (-len(x[1]), x[0])):
            print(f'{user}')
            for m in message:
                print(f'- {m}')
        break
    name = line[1]
    if line[0] == 'Add':
        if name in users:
            print(f'{name} is already registered')
        else:
            users[name] = []
    elif line[0] == 'Send':
        users[name].append(line[2])
    elif line[0] == 'Delete':
        if name in users:
            del users[name]
        else:
            print(f"{name} not found!")
