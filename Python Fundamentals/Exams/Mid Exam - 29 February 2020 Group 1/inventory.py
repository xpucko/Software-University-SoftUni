items = input().split(', ')

while True:
    command = input().split(' - ')
    if command[0] == 'Craft!':
        print(', '.join(items))
        break
    item = command[1]
    if command[0] == 'Collect':
        if item not in items:
            items.append(item)
    elif command[0] == 'Drop':
        if item in items:
            items.remove(item)
    elif command[0] == 'Renew':
        if item in items:
            items.remove(item)
            items.append(item)
    elif command[0] == 'Combine Items':
        old_item = command[1].split(':')[0]
        if old_item in items:
            new_item = command[1].split(':')[1]
            items.insert(items.index(old_item) + 1, new_item)