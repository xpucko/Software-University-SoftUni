def read_matrix():
    return [[x for x in input().split()] for _ in range(int(input()))]


def is_valid(matrix, row, col):
    return row in range(len(matrix)) and col in range(len(matrix))


def get_info(matrix):
    total = 0
    row, col = None, None
    for i in range(len(matrix)):
        if 'p' in matrix[i]:
            row, col = i, matrix[i].index('p')
        if 't' in matrix[i]:
            total += matrix[i].count('t')

    return row, col, total


directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

field = read_matrix()
y, x, targets_left = get_info(field)
targets_total = targets_left
for _ in range(int(input())):
    line = input().split()
    command, direction, steps = line[0], line[1], int(line[2])
    next_y, next_x = y + (directions[direction][0] * steps), x + (directions[direction][1] * steps)
    if is_valid(field, next_y, next_x):
        if command == 'move' and field[next_y][next_x] == '.':
            field[y][x] = '.'
            field[next_y][next_x] = 'p'
            y, x = next_y, next_x
        elif command == 'shoot':
            if field[next_y][next_x] == 't':
                targets_left -= 1
            field[next_y][next_x] = 'x'
            if targets_left == 0:
                print(f'Mission accomplished! All {targets_total} targets destroyed.')
                break

if targets_left > 0:
    print(f'Mission failed! {targets_left} targets left.')
[print(*x) for x in field]
