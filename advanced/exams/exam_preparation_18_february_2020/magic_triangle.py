def get_magic_triangle(n):
    rows = [[1]]
    [rows.append([1] + [sum(pair) for pair in zip(rows[-1], rows[-1][1:])] + [1]) for _ in range(n - 1)]
    return rows
