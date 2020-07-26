username = input()
while True:
    line = input()
    if line == 'Sign up':
        break
    command = line.split()
    if command[0] == 'Case':
        if command[1] == 'lower':
            username = username.lower()
        else:
            username = username.upper()
        print(username)
    elif command[0] == 'Reverse':
        if int(command[1]) in range(len(username)) and int(command[2]) in range(len(username)):
            print(username[int(command[1]):int(command[2]) + 1][::-1])
    elif command[0] == 'Cut':
        if command[1] in username:
            username = username.replace(command[1], '')
            print(username)
        else:
            print(f"The word {username} doesn't contain {command[1]}.")
    elif command[0] == 'Replace':
        username = username.replace(command[1], '*')
        print(username)
    elif command[0] == 'Check':
        print('Valid') if command[1] in username else print(f'Your username must contain {command[1]}.')