m = [[int(x) for x in input().split()] for _ in range(int(input()))]
print(abs(sum([m[x][x] for x in range(len(m))]) - sum([m[x][len(m) - x - 1] for x in range(len(m))])))


# def read_matrix(n):
#     return [[int(x) for x in input().split()] for _ in range(n)]
#
#
# def get_d iagonals_difference_from_matrix(matrix):
#     sum_primary = 0
#     sum_secondary = 0
#
#     for x in range(len(matrix)):
#         sum_primary += matrix[x][x]
#         sum_secondary += matrix[x][len(matrix) - x - 1]
#
#     return abs(sum_primary - sum_secondary)
#
#
# my_matrix = read_matrix(int(input()))
# print(get_diagonals_difference_from_matrix(my_matrix))
