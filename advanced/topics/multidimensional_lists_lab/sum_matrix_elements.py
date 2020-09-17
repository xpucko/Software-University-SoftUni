matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input().split(', ')[0]))]
print(f'{sum([sum(matrix[i]) for i in range(len(matrix))])}\n{matrix}')


# def read_matrix(n):
#     return [[int(x) for x in input().split(', ')] for _ in range(int(n.split(', ')[0]))]
#
#
# def sum_matrix_elements(matrix):
#     return sum([sum(matrix[i]) for i in range(len(matrix))])
#
#
# my_matrix = read_matrix(input())
# print(sum_matrix_elements(my_matrix))
# print(my_matrix)
