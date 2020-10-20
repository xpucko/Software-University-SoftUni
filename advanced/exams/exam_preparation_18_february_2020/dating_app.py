males = [int(x) for x in input().split()]
females = [int(x) for x in input().split()]
matches = 0

while males and females:
    male = males[-1]
    female = females[0]

    if male <= 0:
        males.pop()
        continue
    if female <= 0:
        females.pop(0)
        continue

    if male % 25 == 0:
        males.pop()
        continue
    if female % 25 == 0:
        females.pop(0)
        continue

    if male == female:
        males.pop()
        females.pop(0)
        matches += 1
    else:
        females.pop(0)
        males[-1] -= 2

print(f'Matches: {matches}')

if males:
    print(f'Males left: {", ".join(map(str, reversed(males)))}')
else:
    print('Males left: none')

if females:
    print(f'Females left: {", ".join(map(str, females))}')
else:
    print('Females left: none')
