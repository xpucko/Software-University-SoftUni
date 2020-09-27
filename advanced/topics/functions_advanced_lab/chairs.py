def combinations(names, size, result=None):
    if result is None:
        result = []
    if len(result) == size:
        print(', '.join(result))
        return
    for i in range(len(names)):
        name = names[i]
        result.append(name)
        combinations(names[i + 1:], size, result)
        result.pop()


ll = input().split(', ')
n = int(input())
combinations(ll, n)