string = input()

while True:
    line = input().split(':')
    if line[0] == 'Travel':
        print(f'Ready for world tour! Planned stops: {string}')
        break
    elif line[0] == 'Add Stop':
        if int(line[1]) in range(len(string)):
            string = string[:int(line[1])] + line[2] + string[int(line[1]):]
        print(string)
    elif line[0] == 'Remove Stop':
        if int(line[1]) in range(len(string)) and int(line[2]) in range(len(string)):
            string = string[:int(line[1])] + string[int(line[2]) + 1:]
        print(string)
    elif line[0] == 'Switch':
        if line[1] in string:
            string = string.replace(line[1], line[2])
        print(string)
