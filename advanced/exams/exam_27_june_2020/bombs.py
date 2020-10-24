effects = [int(x) for x in input().split(', ')]
casings = [int(x) for x in input().split(', ')]
materials = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}
result = {'Cherry Bombs': 0, 'Datura Bombs': 0, 'Smoke Decoy Bombs': 0}
is_full = False

while effects and casings and not is_full:
    if effects[0] + casings[-1] in materials:
        result[materials[effects[0] + casings[-1]]] += 1
        effects.pop(0)
        casings.pop()
    else:
        casings[-1] -= 5

    count = 0
    for k, v in result.items():
        if v > 2:
            count += 1
    if count == 3:
        is_full = True

if not is_full:
    print("You don't have enough materials to fill the bomb pouch.")
else:
    print('Bene! You have successfully filled the bomb pouch!')
if effects:
    print(f'Bomb Effects: {", ".join(map(str, effects))}')
else:
    print('Bomb Effects: empty')
if casings:
    print(f'Bomb Casings: {", ".join(map(str, casings))}')
else:
    print('Bomb Casings: empty')

for k, v in result.items():
    print(f'{k}: {v}')
