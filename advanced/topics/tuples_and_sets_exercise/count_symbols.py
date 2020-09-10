string = input()
[print(f'{ch}: {string.count(ch)} time/s') for ch in sorted(set(string))]