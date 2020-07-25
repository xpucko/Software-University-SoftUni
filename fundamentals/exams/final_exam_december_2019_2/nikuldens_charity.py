string = input()
while True:
    data = input().split()
    if data[0] == 'Finish':
        break
    elif data[0] == 'Replace':
        string = string.replace(data[1], data[2])
        print(string)
    elif data[0] == 'Cut':
        if int(data[1]) in range(len(string)) and int(data[2]) in range(len(string)):
            string = string[:int(data[1])] + string[int(data[2]) + 1:]
            print(string)
        else:
            print('Invalid indexes!')
    elif data[0] == 'Make':
        string = string.upper() if data[1] == 'Upper' else string.lower()
        print(string)
    elif data[0] == 'Check':
        print(f'Message contains {data[1]}') if data[1] in string else print(f"Message doesn't contain {data[1]}")
    elif data[0] == 'Sum':
        if int(data[1]) in range(len(string)) and int(data[2]) in range(len(string)):
            print(sum([ord(ch) for ch in string[int(data[1]):int(data[2]) + 1]]))
        else:
            print('Invalid indexes!')
