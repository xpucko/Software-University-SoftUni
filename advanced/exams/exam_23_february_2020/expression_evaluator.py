def operate(operator, numbers):
    result = numbers[0]
    if operator == '-':
        for x in numbers[1:]:
            result -= x
    elif operator == '*':
        for x in numbers[1:]:
            result *= x
    elif operator == '/':
        for x in numbers[1:]:
            result //= x
    else:
        result = sum(numbers)

    return result


expression = input().split()
nums = []
for current in expression:
    if current not in ['+', '-', '*', '/']:
        nums.append(int(current))
    else:
        nums = [operate(current, nums)]

print(*nums)
