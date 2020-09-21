def read_matrix():
    return [[int(x) for x in input().split()] for _ in range(int(input()))]


def explode(matrix):
    line = input().split()
    for i in range(len(line)):
        x, y = [int(n) for n in line[i].split(',')]
        if matrix[x][y] > 0:
            coordinates = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
            for j in range(8):
                row_count = x + coordinates[j][0]
                column_count = y + coordinates[j][1]
                if row_count in range(len(matrix)) and column_count in range(len(matrix)):
                    if matrix[row_count][column_count] > 0:
                        matrix[row_count][column_count] -= matrix[x][y]
            matrix[x][y] = 0

    return matrix


def print_result(matrix):
    alive_cells = 0
    sum_alive_cells = 0
    for i in matrix:
        for j in i:
            if j > 0:
                alive_cells += 1
                sum_alive_cells += j

    print(f'Alive cells: {alive_cells}\nSum: {sum_alive_cells}')
    [print(" ".join(map(str, x))) for x in matrix]


print_result(explode(read_matrix()))
