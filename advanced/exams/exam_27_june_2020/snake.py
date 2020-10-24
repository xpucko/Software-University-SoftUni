def read_matrix():
    return [[ch for ch in input()] for _ in range(int(input()))]


def is_valid(matrix, row_index, col_index):
    return row_index in range(len(matrix)) and col_index in range(len(matrix))


def get_info(matrix):
    row, col = None, None
    ll = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'S':
                row, col = i, j
            if matrix[i][j] == 'B':
                ll.append([i, j])

    return row, col, ll


field = read_matrix()
y, x, lairs = get_info(field)
food = 0
directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

while True:
    command = input()
    next_y, next_x = y + directions[command][0], x + directions[command][1]

    if is_valid(field, next_y, next_x):
        field[y][x] = '.'

        if field[next_y][next_x] == '*':
            y, x = next_y, next_x
            field[y][x] = 'S'
            food += 1
            if food == 10:
                print('You won! You fed the snake.')
                break

        elif field[next_y][next_x] == 'B':
            field[next_y][next_x] = '.'
            for lair in lairs:
                if next_y != lair[0] and next_x != lair[1]:
                    y, x = lair[0], lair[1]
                    field[y][x] = 'S'

        else:
            y, x = next_y, next_x
            field[y][x] = 'S'

    else:
        field[y][x] = '.'
        print('Game over!')
        break

print(f'Food eaten: {food}')
[print(''.join(x)) for x in field]