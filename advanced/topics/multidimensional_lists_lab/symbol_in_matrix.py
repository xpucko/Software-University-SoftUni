def read_matrix(n):
    matrix = []
    for _ in range(n):
        row = []
        [row.append(ch) for ch in input()]
        matrix.append(row)
    return matrix


def find_first_occurrence(matrix):
    symbol = input()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == symbol:
                return f'({i}, {j})'
    return f'{symbol} does not occur in the matrix'


print(find_first_occurrence(read_matrix(int(input()))))