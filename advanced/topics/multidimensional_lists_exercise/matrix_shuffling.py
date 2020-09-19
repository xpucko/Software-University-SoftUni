def read_matrix():
    return [input().split() for _ in range(int(input().split()[0]))]


def swap_places_in_matrix_and_print_result(matrix):
    while True:
        line = input().split()
        if line[0] == 'END':
            return
        elif line[0] != 'swap' or len(line) != 5:
            print('Invalid input!')
        else:
            row_1, col_1, row_2, col_2 = int(line[1]), int(line[2]), int(line[3]), int(line[4])
            if row_1 >= len(matrix) or row_2 >= len(matrix) or col_1 >= len(matrix[0]) or col_2 >= len(matrix[0]):
                print('Invalid input!')
            else:
                matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
                [print(' '.join(map(str, x))) for x in matrix]


swap_places_in_matrix_and_print_result(read_matrix())
