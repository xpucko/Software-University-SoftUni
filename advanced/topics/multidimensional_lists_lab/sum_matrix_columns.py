def read_matrix(separator):
    rows_count, columns_count = [int(x) for x in input().split(', ')]
    return [[int(x) for x in input().split(separator)] for _ in range(rows_count)]


def get_column_sums(matrix):
    rows_count = len(matrix)
    column_count = len(matrix[0])
    column_sum = [0] * column_count

    for row in range(rows_count):
        for column in range(column_count):
            column_sum[column] += matrix[row][column]

    return column_sum


my_matrix = read_matrix(' ')
columns_sums = get_column_sums(my_matrix)
[print(x) for x in columns_sums]