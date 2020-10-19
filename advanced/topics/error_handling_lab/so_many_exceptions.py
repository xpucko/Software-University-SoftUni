numbers_list = [int(x) for x in input().split(', ')]
result = 1

for x in numbers_list:
    if x <= 5:
        result *= x
    elif x < 11:
        result /= x

print(result)
