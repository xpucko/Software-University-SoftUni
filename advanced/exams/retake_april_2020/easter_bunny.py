def read_matrix():
    return [[x for x in input().split()] for _ in range(int(input()))]


def is_valid(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix) and matrix[row][col] != 'X'


def get_info(matrix):
    row, col = None, None
    traps_count = 0
    for i in range(len(matrix)):
        if 'B' in matrix[i]:
            row, col = i, matrix[i].index('B')
        if 'X' in matrix[i]:
            traps_count += matrix[i].count('X')

    return row, col, traps_count


field = read_matrix()
start_y, start_x, traps = get_info(field)
directions = ['up', 'down', 'left', 'right']
best_sum = 0
best_moves = []
best_direction = None

for i in range(len(directions)):
    current_moves = []
    current_sum = 0
    y, x = start_y, start_x
    next_y, next_x = start_y, start_x

    while True:
        if directions[i] == 'up':
            next_y, next_x = y - 1, x
        elif directions[i] == 'down':
            next_y, next_x = y + 1, x
        elif directions[i] == 'left':
            next_y, next_x = y, x - 1
        elif directions[i] == 'right':
            next_y, next_x = y, x + 1
        y, x = next_y, next_x

        if is_valid(field, next_y, next_x):
            current_sum += int(field[next_y][next_x])
            current_moves.append([next_y, next_x])
        else:
            if current_sum >= best_sum:
                best_sum = current_sum
                best_moves = current_moves
                best_direction = directions[i]
            break

print(best_direction)
[print(x) for x in best_moves]
print(best_sum)
