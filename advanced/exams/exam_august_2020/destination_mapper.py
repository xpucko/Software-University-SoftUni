import re

pattern = r'=[A-Z][a-zA-Z]{2,}=|\/[A-Z][a-zA-Z]{2,}\/'
data = input()
matched = re.findall(pattern, data)
destinations = []
points = 0
if matched:
    for i in range(len(matched)):
        points += len(matched[i]) - 2
        destinations.append(matched[i][1:-1])
print(f'Destinations: {", ".join(destinations)}')
print(f'Travel Points: {points}')
