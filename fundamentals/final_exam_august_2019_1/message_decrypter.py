import re

pattern = r'^([$|%])([A-Z][a-z]{2,})\1: (\[[\d]+\]\|\[[\d]+\]\|\[[\d]+\]\|)$'
for _ in range(int(input())):
    line = input()
    match = re.findall(pattern, line)
    if not match:
        print('Valid message not found!')
    else:
        numbers_str = match[0][2].split('|')
        x = int(numbers_str[0][1:-1])
        y = int(numbers_str[1][1:-1])
        z = int(numbers_str[2][1:-1])
        print(f'{match[0][1]}: {chr(x)}{chr(y)}{chr(z)}')