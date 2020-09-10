elements = set()
for _ in range(int(input())):
    elements |= set(input().split())
[print(x) for x in elements]