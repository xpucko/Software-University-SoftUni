from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

presents = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
result = {'Bicycle': 0, 'Doll': 0, 'Teddy bear': 0, 'Wooden train': 0}

while materials and magic:
    current_material = materials[-1]
    current_magic = magic[0]
    multiplication = current_material * current_magic

    if multiplication == 0:
        if current_material == 0:
            materials.pop()
        if current_magic == 0:
            magic.popleft()
        continue
    elif multiplication in presents:
        current_present = presents[multiplication]
        result[current_present] += 1
        materials.pop()
        magic.popleft()
    else:
        if multiplication < 0:
            the_sum = current_magic + current_material
            materials.pop()
            magic.popleft()
            materials.append(the_sum)
        else:
            magic.popleft()
            materials[-1] += 15

if (result['Doll'] > 0 and result['Wooden train'] > 0) or (result['Teddy bear'] > 0 and result['Bicycle'] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for k, v in result.items():
    if v > 0:
        print(f"{k}: {v}")
