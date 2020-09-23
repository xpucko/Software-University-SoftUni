def get_info():
    n = int(input())
    commands = input().split()
    miner_position = []
    total_coals = 0
    matrix = []
    for i in range(n):
        current_row = input().split()
        matrix.append(current_row)
        if 's' in current_row:
            miner_position = [i, current_row.index('s')]
        total_coals += current_row.count('c')

    return commands, [x for x in matrix], miner_position, total_coals


def run_commands_and_return_result(commands, matrix, miner_position, total_coals):
    coals = 0
    next_miner_position = []

    for command in commands:
        if command == 'up':
            next_miner_position = [miner_position[0] - 1, miner_position[1]]
        elif command == 'down':
            next_miner_position = [miner_position[0] + 1, miner_position[1]]
        elif command == 'left':
            next_miner_position = [miner_position[0], miner_position[1] - 1]
        elif command == 'right':
            next_miner_position = [miner_position[0], miner_position[1] + 1]

        row_count = next_miner_position[0]
        col_count = next_miner_position[1]

        if 0 <= row_count < len(matrix) and 0 <= col_count < len(matrix):
            if matrix[row_count][col_count] == 'e':
                return f'Game over! ({row_count}, {col_count})'
            elif matrix[row_count][col_count] == 'c':
                coals += 1
                if coals == total_coals:
                    return f'You collected all coals! ({row_count}, {col_count})'
            matrix[miner_position[0]][miner_position[1]] = '*'
            matrix[row_count][col_count] = 's'
            miner_position = next_miner_position

    return f'{total_coals - coals} coals left. ({miner_position[0]}, {miner_position[1]})'


current_commands, my_matrix, miner_pos, total_c = get_info()
print(run_commands_and_return_result(current_commands, my_matrix, miner_pos, total_c))
