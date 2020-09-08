clothes = [int(x) for x in input().split()]
rack_limit = int(input())
total_racks = 1
current_rack = 0

while clothes:
    current = clothes.pop()
    current_rack += current
    if current_rack > rack_limit:
        clothes.append(current)
        total_racks += 1
        current_rack = 0

print(total_racks)