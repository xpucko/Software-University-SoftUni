numbers = sorted(map(int, input().split()), reverse=True)
average = sum(numbers) / len(numbers)
result = []
[result.append(number) for number in numbers if number > average and len(result) < 5]
if result:
    print(*result)
else:
    print('No')
