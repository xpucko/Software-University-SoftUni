def read_matrix():
    return [[x for x in input().split()] for _ in range(int(input()))]


def get_info(matrix):
    total = 0
    santa_position = []
    for i in range(len(matrix)):
        if 'S' in matrix[i]:
            santa_position = [i, matrix[i].index('S')]
        if 'V' in matrix[i]:
            total += matrix[i].count('V')
    return santa_position, total


def is_valid(matrix, row, col):
    return row in range(len(matrix)) and col in range(len(matrix))


presents = int(input())
field = read_matrix()
santa_pos, nice_kids_left = get_info(field)
total_nice_kids = nice_kids_left
directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}
while presents > 0:
    command = input()
    if command == 'Christmas morning':
        break

    y, x = directions[command]
    current_row, current_col = santa_pos
    next_row, next_col = current_row + y, current_col + x

    if is_valid(field, next_row, next_col):
        if field[next_row][next_col] == 'V':
            field[next_row][next_col] = '-'
            presents -= 1
            nice_kids_left -= 1
        elif field[next_row][next_col] == 'C':
            for y, x in directions.values():
                if field[next_row + y][next_col + x] == 'V' or field[next_row + y][next_col + x] == 'X':
                    presents -= 1
                if field[next_row + y][next_col + x] == 'V':
                    nice_kids_left -= 1
                field[next_row + y][next_col + x] = '-'
        field[current_row][current_col] = '-'
        santa_pos = next_row, next_col
        field[next_row][next_col] = 'S'

if presents <= 0 < nice_kids_left:
    print('Santa ran out of presents!')

[print(' '.join(x)) for x in field]

if nice_kids_left <= 0:
    print(f'Good job, Santa! {total_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids_left} nice kid/s.')
