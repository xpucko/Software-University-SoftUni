def is_valid(matrix, row_index, col_index):
    return row_index in range(len(matrix)) and col_index in range(len(matrix))


def read_data():
    string = input()
    size = int(input())
    matrix = []
    player_pos = None
    for i in range(size):
        row = input()
        matrix.append([x for x in row])
        if 'P' in row:
            player_pos = [i, row.index('P')]

    return string, matrix, player_pos


def play(string, matrix, player_pos):
    player_current = player_pos
    directions = {
        'up': [-1, 0],
        'down': [1, 0],
        'left': [0, -1],
        'right': [0, 1],
    }
    for _ in range(int(input())):
        direction = input()
        player_next = [player_current[0] + directions[direction][0], player_current[1] + directions[direction][1]]
        if is_valid(matrix, player_next[0], player_next[1]):
            if matrix[player_next[0]][player_next[1]] != '-':
                string += matrix[player_next[0]][player_next[1]]
            matrix[player_current[0]][player_current[1]] = '-'
            matrix[player_next[0]][player_next[1]] = 'P'
            player_current = player_next
        else:
            string = string[:-1]

    return string, matrix


word, field, player = read_data()
worm, result = play(word, field, player)
print(worm)
[print(''.join(x)) for x in result]