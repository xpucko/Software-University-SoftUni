import re

pattern = r'\|([A-Z]{4,})\|:#([a-zA-Z]{1,} [a-zA-Z]{1,})#'

for _ in range(int(input())):
    matched = re.findall(pattern, input())
    if not matched:
        print('Access denied!')
    else:
        print(f'{matched[0][0]}, The {matched[0][1]}')
        print(f'>> Strength: {len(matched[0][0])}')
        print(f'>> Armour: {len(matched[0][1])}')