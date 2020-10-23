def read_matrix():
    size = int(input())
    return [[0] * size for _ in range(size)]


def is_valid(matrix, next_row, next_col):
    return 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix) and matrix[next_row][next_col] != '*'


def get_bombs_pos():
    return [[int(x) for x in input().strip('()').split(', ')] for _ in range(int(input()))]


def explode_bombs(matrix, bombs_positions):
    exp = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for bomb_pos in bombs_positions:
        y, x = bomb_pos[0], bomb_pos[1]
        field[y][x] = '*'
        for current in exp:
            next_y, next_x = y + current[0], x + current[1]
            if is_valid(field, next_y, next_x):
                field[next_y][next_x] += 1

    return matrix


def print_field(matrix):
    return [print(' '.join(map(str, x))) for x in matrix]


field = read_matrix()
bombs_pos = get_bombs_pos()
explode_bombs(field, bombs_pos)
print_field(field)
