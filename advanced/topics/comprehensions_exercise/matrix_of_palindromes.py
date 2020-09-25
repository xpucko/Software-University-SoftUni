rows, cols = [int(x) for x in input().split()]
matrix = [[f'{chr(row)}{chr(row + col)}{chr(row)}' for col in range(cols)] for row in range(97, 97 + rows)]
[print(' '.join(x)) for x in matrix]
