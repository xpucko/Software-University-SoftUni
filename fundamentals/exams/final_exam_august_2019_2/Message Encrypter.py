import re

pattern = r'([*|@])([A-Z][a-z]{2,})\1: (\[[A-Za-z]+\]\|\[[A-Za-z]\]\|\[[A-Za-z]+\]\|)$'
for _ in range(int(input())):
    data = input()
    match = re.findall(pattern, data)
    if not match:
        print('Valid message not found!')
    else:
        matched = match[0][2].split('|')
        print(f'{match[0][1]}: {ord(matched[0][1:-1])} {ord(matched[1][1:-1])} {ord(matched[2][1:-1])}')
