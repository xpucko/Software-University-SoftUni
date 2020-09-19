from collections import deque


def read_empty_matrix():
    rows_count, columns_count = [int(x) for x in input().split()]
    return [['' for _ in range(columns_count)] for _ in range(rows_count)]


def fill_empty_matrix_with_characters_from_string(matrix):
    string = deque(input())
    for row_count in range(len(matrix)):
        for col_count in range(len(matrix[0])):
            ch = string.popleft()
            matrix[row_count][col_count] = ch
            string.append(ch)
        if row_count % 2 != 0:
            matrix[row_count] = matrix[row_count][::-1]

    return matrix


def print_matrix(matrix):
    return [print(''.join(x)) for x in matrix]


print_matrix(fill_empty_matrix_with_characters_from_string(read_empty_matrix()))
