def get_empty_matrix(size):
    return [[0 for _ in range(size)] for _ in range(size)]


def get_bombs_coordinates(count):
    return [[int(x) for x in input().strip('()').split(', ')] for _ in range(count)]


def is_valid(row_count, col_count, matrix):
    return row_count in range(len(matrix)) and col_count in range(len(matrix))


def get_matrix_before_explode(matrix, coordinates):
    for current in coordinates:
        row_count, col_count = current[0], current[1]
        matrix[row_count][col_count] = '*'

    return matrix


def explode_bombs(matrix, bombs_positions):
    for current_pos in bombs_positions:
        row_count, col_count = current_pos[0], current_pos[1]
        for x in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
            possible_row, possible_col = x[0] + row_count, x[1] + col_count
            if is_valid(possible_row, possible_col, matrix) and matrix[possible_row][possible_col] != '*':
                matrix[possible_row][possible_col] += 1

    return matrix


empty_field = get_empty_matrix(int(input()))
bombs_pos = get_bombs_coordinates(int(input()))
field = get_matrix_before_explode(empty_field, bombs_pos)
exploded_field = explode_bombs(field, bombs_pos)
[print(' '.join(map(str, row))) for row in exploded_field]
