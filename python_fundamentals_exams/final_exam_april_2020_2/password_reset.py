password = input()
while True:
    line = input().split()
    if line[0] == 'Done':
        print(f'Your password is: {password}')
        break
    elif line[0] == 'TakeOdd':
        new = ''
        for i in range(len(password)):
            if i % 2 == 1:
                new += password[i:i + 1]
        password = new
        print(password)
    elif line[0] == 'Cut':
        password = password[:int(line[1])] + password[int(line[1]) + int(line[2]):]
        print(password)
    elif line[0] == 'Substitute':
        if line[1] in password:
            password = password.replace(line[1], line[2])
            print(password)
        else:
            print('Nothing to replace!')