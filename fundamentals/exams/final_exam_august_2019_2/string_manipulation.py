string = input()
while True:
    command = input().split()
    if command[0] == 'Done':
        break
    elif command[0] == 'Change':
        string = string.replace(command[1], command[2])
        print(string)
    elif command[0] == 'Includes':
        print(True) if command[1] in string else print(False)
    elif command[0] == 'End':
        print(True) if command[1] == string[len(string) - len(command[1]):] else print(False)
    elif command[0] == 'Uppercase':
        string = string.upper()
        print(string)
    elif command[0] == 'FindIndex':
        print(string.find(command[1]))
    elif command[0] == 'Cut':
        string = string[int(command[1]): int(command[1]) + int(command[2])]
        print(string)
