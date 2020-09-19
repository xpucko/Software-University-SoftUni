def read_matrix():
    size, _ = [int(x) for x in input().split()]
    return [[int(x) for x in input().split()] for _ in range(size)]


def find_biggest_3x3_matrix(matrix):
    best_sum = -1
    best_matrix_3x3 = None
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[i]) - 2):
            current_matrix = [
                [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
                [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
                [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]],
            ]
            current_sum = sum(sum(m) for m in current_matrix)
            if current_sum > best_sum:
                best_sum = current_sum
                best_matrix_3x3 = current_matrix

    return best_sum, best_matrix_3x3


def print_sum_and_biggest_3x3_matrix():
    sum_result, matrix_result = find_biggest_3x3_matrix(read_matrix())
    print(f'Sum = {sum_result}')
    [print(' '.join(map(str, x))) for x in matrix_result]


print_sum_and_biggest_3x3_matrix()
