def read_matrix(cells_delimiter):
    n = int(input())
    return [list(map(int, input().split(cells_delimiter))) for _ in range(n)]


def diagonal_difference(matrix):
    sum_primary = 0
    sum_secondary = 0
    for x in range(len(matrix)):
        sum_primary += matrix[x][x]
        sum_secondary += matrix[x][len(matrix) - x - 1]
    difference = abs(sum_primary - sum_secondary)
    return difference


my_matrix = read_matrix(' ')
print(diagonal_difference(my_matrix))
