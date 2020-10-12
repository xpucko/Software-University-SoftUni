with open('text.txt', 'r') as file:
    [print(' '.join(line.translate(line.maketrans("-,.!?", "@@@@@")).split()[::-1])) for i, line in enumerate(file) if i % 2 == 0]