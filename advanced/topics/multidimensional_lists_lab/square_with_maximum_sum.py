def read_matrix(separator):
    rows_count, columns_count = [int(x) for x in input().split(', ')]
    return [[int(x) for x in input().split(separator)] for _ in range(rows_count)]


def find_best_matrix_2x2_and_sum(matrix):
    best_sum = 0
    best_matrix_2x2 = None

    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            a = matrix[i][j]
            b = matrix[i][j + 1]
            c = matrix[i + 1][j]
            d = matrix[i + 1][j + 1]
            current_sum = sum([a, b, c, d])

            if current_sum > best_sum:
                best_sum = current_sum
                best_matrix_2x2 = [[a, b], [c, d]]

    return best_sum, best_matrix_2x2


the_sum, the_matrix = find_best_matrix_2x2_and_sum(read_matrix(', '))
[print(*x) for x in the_matrix]
print(the_sum)
