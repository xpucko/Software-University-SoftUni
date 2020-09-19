def read_board():
    return [[ch for ch in input()] for _ in range(int(input()))]


def is_valid(position, size):
    return 0 <= position[0] < size and 0 <= position[1] < size


def get_killed_knights(row, col, size, board):
    killed = 0
    knight_move = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
    for i in range(len(knight_move)):
        current_position = [row + knight_move[i][0], col + knight_move[i][1]]
        if is_valid(current_position, size) and board[current_position[0]][current_position[1]] == 'K':
            killed += 1

    return killed


matrix = read_board()
total_kills = 0
while True:
    most_kills = 0
    to_kill = []

    for row_count in range(len(matrix)):
        for col_count in range(len(matrix[row_count])):
            if matrix[row_count][col_count] == 'K':
                killed_knights = get_killed_knights(row_count, col_count, len(matrix), matrix)
                if killed_knights > most_kills:
                    most_kills = killed_knights
                    to_kill = [row_count, col_count]

    if most_kills == 0:
        break

    matrix[to_kill[0]][to_kill[1]] = '0'
    total_kills += 1
print(total_kills)