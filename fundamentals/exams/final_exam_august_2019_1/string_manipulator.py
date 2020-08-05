string = input()
while True:
    command = input().split()
    if command[0] == 'End':
        break
    elif command[0] == 'Translate':
        string = string.replace(command[1], command[2])
        print(string)
    elif command[0] == 'Includes':
        print(True) if command[1] in string else print(False)
    elif command[0] == 'Start':
        print(True) if string[:len(command[1])] == command[1] else print(False)
    elif command[0] == 'Lowercase':
        string = string.lower()
        print(string)
    elif command[0] == 'FindIndex':
        print(abs(string[::-1].index(command[1]) - len(string) + 1))
    elif command[0] == 'Remove':
        index = int(command[1])
        count = int(command[2])
        string = string[:index] + string[index + count:]
        print(string)