def get_matrix():
    return [[int(x) for x in input().split()] for _ in range(int(input()))]


def is_valid_index(row_count, col_count, matrix):
    return 0 <= row_count < len(matrix) and 0 <= col_count < len(matrix)


def modify_matrix_until_command(command, matrix):
    while True:
        line = input().split()
        if line[0] == command:
            return matrix
        operation = line[0]
        row = int(line[1])
        col = int(line[2])
        value = int((line[3]))
        if is_valid_index(row, col, matrix):
            if operation == 'Add':
                matrix[row][col] += value
            elif operation == 'Subtract':
                matrix[row][col] -= value
        else:
            print('Invalid coordinates')


def print_modified_matrix(matrix):
    return [print(' '.join([str(x) for x in row])) for row in matrix]


my_matrix = get_matrix()
modify_matrix_until_command('END', my_matrix)
print_modified_matrix(my_matrix)
