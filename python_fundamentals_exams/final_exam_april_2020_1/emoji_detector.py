import re
from functools import reduce

pattern = r'([:]{2}|[*]{2})([A-Z][a-z]{2,})\1'
data = input()
smiles = re.findall(pattern, data)
cool_threshold = reduce((lambda x, y: x * y), [int(ch) for ch in data if ch.isdigit()])

print(f'Cool threshold: {cool_threshold}')
print(f'{len(smiles)} emojis found in the text. The cool ones are:')
for i in range(len(smiles)):
    if sum([ord(ch) for ch in smiles[i][1]]) >= cool_threshold:
        print(f'{smiles[i][0] + smiles[i][1] + smiles[i][0]}')