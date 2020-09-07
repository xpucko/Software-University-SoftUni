parts = input().split('|')
while True:
    command = input().split()
    if command[0] == 'Done':
        print(f"You crafted {''.join(parts)}!")
        break
    if command[0] == 'Move':
        index = int(command[2])
        if command[1] == 'Left' and index in range(1, len(parts)):
            parts[index - 1], parts[index] = parts[index], parts[index - 1]
        elif command[1] == 'Right' and index in range(len(parts) - 1):
            parts[index], parts[index + 1] = parts[index + 1], parts[index]
    elif command[1] == 'Even':
        even_elements = []
        [even_elements.append(parts[i]) for i in range(len(parts)) if i % 2 == 0]
        print(*even_elements)
    elif command[1] == 'Odd':
        odd_elements = []
        [odd_elements.append(parts[i]) for i in range(len(parts)) if i % 2 == 1]
        print(*odd_elements)