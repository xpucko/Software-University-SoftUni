longest_intersection = []
for _ in range(int(input())):
    data = input().split('-')
    first = [int(x) for x in data[0].split(',')]
    second = [int(x) for x in data[1].split(',')]
    first_set = set([x for x in range(first[0], first[1] + 1)])
    second_set = set([x for x in range(second[0], second[1] + 1)])
    current = first_set.intersection(second_set)
    if len(current) > len(longest_intersection):
        longest_intersection = current
print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')