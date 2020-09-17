def read_matrix(separator):
    n = int(input())
    return [[int(x) for x in input().split(separator)] for _ in range(n)]


def sum_primary_diagonal(matrix):
    return sum([matrix[x][x] for x in range(len(matrix))])


my_matrix = read_matrix(' ')
print(sum_primary_diagonal(my_matrix))
