def read_matrix():
    return [[row for row in input().split()] for _ in range(8)]


def get_king_coordinates(matrix):
    for row_count in range(len(matrix)):
        if 'K' in matrix[row_count]:
            return row_count, matrix[row_count].index('K')


def is_valid(matrix, row_index, col_index):
    return row_index in range(len(matrix)) and col_index in range(len(matrix))


field = read_matrix()
y, x = get_king_coordinates(field)
result = []
directions = [[-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1], [-1, -1]]

for i in range(8):
    next_y, next_x = y + directions[i][0], x + directions[i][1]
    while is_valid(field, next_y, next_x):
        if field[next_y][next_x] == 'Q':
            result.append([next_y, next_x])
            break
        next_y, next_x = next_y + directions[i][0], next_x + directions[i][1]

[print(x) for x in result] if result else print('The king is safe!')
