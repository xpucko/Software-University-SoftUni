def read_matrix(cells_delimiter):
    rows_count, columns_count = map(int, input().split())
    return [input().split(cells_delimiter) for _ in range(rows_count)]


def find_squares_equal_chairs(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    counter = 0
    for row in range(rows_count - 1):
        for column in range(columns_count - 1):
            if matrix[row][column] == matrix[row][column + 1] == matrix[row + 1][column] == matrix[row + 1][column + 1]:
                counter += 1
    return counter


my_matrix = read_matrix(' ')
print(find_squares_equal_chairs(my_matrix))
