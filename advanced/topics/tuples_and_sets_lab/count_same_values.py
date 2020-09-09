numbers = [float(x) for x in input().split()]
result = {}
for number in numbers:
    if number not in result:
        result[number] = 0
    result[number] += 1

for k, v in result.items():
    print(f'{k} - {v} times')