data = input()
while True:
    command = input().split('>>>')
    if command[0] == 'Generate':
        print(f'Your activation key is: {data}')
        break
    elif command[0] == 'Contains':
        print(f'{data} contains {command[1]}') if command[1] in data else print('Substring not found!')
    elif command[0] == 'Flip':
        case = command[1]
        index_start = int(command[2])
        index_end = int(command[3])
        if case == 'Upper':
            data = data[:index_start] + data[index_start:index_end].upper() + data[index_end:]
        else:
            data = data[:index_start] + data[index_start:index_end].lower() + data[index_end:]
        print(data)
    elif command[0] == 'Slice':
        start = int(command[1])
        end = int(command[2])
        data = data[:start] + data[end:]
        print(data)