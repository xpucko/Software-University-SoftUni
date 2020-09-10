set_n = set()
set_m = set()
n, m = [int(x) for x in input().split()]
[set_n.add(int(input())) for _ in range(n)]
[set_m.add(int(input())) for _ in range(m)]
[print(x) for x in set_n.intersection(set_m)]