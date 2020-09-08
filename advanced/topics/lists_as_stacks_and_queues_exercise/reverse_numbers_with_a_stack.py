n = list(map(int, input().split()))
result = []
for _ in range(len(n)):
    current = n.pop()
    result.append(current)
print(*result)