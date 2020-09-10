set_odd = set()
set_even = set()

for i in range(int(input())):
    summed = sum([ord(ch) for ch in input()]) // (i + 1)
    set_even.add(summed) if summed % 2 == 0 else set_odd.add(summed)

if sum(set_odd) < sum(set_even):
    print(', '.join(map(str, set_odd.symmetric_difference(set_even))))
elif sum(set_odd) == sum(set_even):
    print(', '.join(map(str, set_odd.union(set_even))))
else:
    print(', '.join(map(str , set_odd.difference(set_even))))