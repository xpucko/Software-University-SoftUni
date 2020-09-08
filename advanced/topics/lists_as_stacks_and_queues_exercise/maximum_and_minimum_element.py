result = []
for _ in range(int(input())):
    command = [int(x) for x in input().split()]
    if command[0] == 1:
        result.append(command[1])
    if result:
        if command[0] == 2:
            result.pop()
        elif command[0] == 3:
            print(max(result))
        elif command[0] == 4:
            print(min(result))

print(', '.join([str(x) for x in reversed(result)]))
