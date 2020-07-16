numbers = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == 'end':
        print(', '.join(map(str, numbers)))
        break
    elif command[0] == 'decrease':
        numbers = [x - 1 for x in numbers]
    elif command[0] == 'swap':
        numbers[int(command[1])], numbers[int(command[2])] = numbers[int(command[2])], numbers[int(command[1])]
    elif command[0] == 'multiply':
        numbers[int(command[1])] *= numbers[int(command[2])]