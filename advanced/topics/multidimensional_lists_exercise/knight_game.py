def read_board():
    return [[ch for ch in input()] for _ in range(int(input()))]


def get_damage(row_count, column_count, matrix):
    counter = 0
    if row_count - 2 >= 0 and column_count - 1 >= 0:
        if matrix[row_count - 2][column_count - 1] == 'K':
            counter += 1
    if row_count - 2 >= 0 and column_count + 1 < len(matrix):
        if matrix[row_count - 2][column_count + 1] == 'K':
            counter += 1
    if row_count - 1 >= 0 and column_count - 2 >= 0:
        if matrix[row_count - 1][column_count - 2] == 'K':
            counter += 1
    if row_count - 1 >= 0 and column_count + 2 < len(matrix):
        if matrix[row_count - 1][column_count + 2] == 'K':
            counter += 1
    if row_count + 1 < len(matrix) and column_count - 2 >= 0:
        if matrix[row_count + 1][column_count - 2] == 'K':
            counter += 1
    if row_count + 1 < len(matrix) and column_count + 2 < len(matrix):
        if matrix[row_count + 1][column_count + 2] == 'K':
            counter += 1
    if row_count + 2 < len(matrix) and column_count - 1 >= 0:
        if matrix[row_count + 2][column_count - 1] == 'K':
            counter += 1
    if row_count + 2 < len(matrix) and column_count + 1 < len(matrix):
        if matrix[row_count + 2][column_count + 1] == 'K':
            counter += 1
    return counter


def get_count_deleted_knights(matrix):
    position = []
    deleted_knights = 0

    while True:
        max_damage = 0
        for row_index in range(len(matrix)):
            for column_index in range(len(matrix)):
                current = matrix[row_index][column_index]
                if current == 'K':
                    damage = get_damage(row_index, column_index, matrix)
                    if damage > max_damage:
                        max_damage = damage
                        position = [row_index, column_index]

        if max_damage == 0:
            break
        row = position[0]
        column = position[1]
        matrix[row][column] = '0'
        position = []
        deleted_knights += 1

    return deleted_knights


print(get_count_deleted_knights(read_board()))

# def read_board():
#     return [[ch for ch in input()] for _ in range(int(input()))]
#
#
# def is_valid(position, size):
#     return 0 <= position[0] < size and 0 <= position[1] < size
#
#
# def get_killed_knights(row, col, size, board):
#     killed = 0
#     knight_move = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
#     for i in range(len(knight_move)):
#         current_position = [row + knight_move[i][0], col + knight_move[i][1]]
#         if is_valid(current_position, size) and board[current_position[0]][current_position[1]] == 'K':
#             killed += 1
#
#     return killed
#
#
# matrix = read_board()
# total_kills = 0
# while True:
#     most_kills = 0
#     to_kill = []
#
#     for row_count in range(len(matrix)):
#         for col_count in range(len(matrix[row_count])):
#             if matrix[row_count][col_count] == 'K':
#                 killed_knights = get_killed_knights(row_count, col_count, len(matrix), matrix)
#                 if killed_knights > most_kills:
#                     most_kills = killed_knights
#                     to_kill = [row_count, col_count]
#
#     if most_kills == 0:
#         break
#
#     matrix[to_kill[0]][to_kill[1]] = '0'
#     total_kills += 1
# print(total_kills)