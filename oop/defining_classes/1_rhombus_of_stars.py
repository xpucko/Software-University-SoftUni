def generate_line(index, n):
    white_spaces = ' ' * (n - index - 1)
    stars = '* ' * (index + 1)
    return f'{white_spaces}{stars}'


def print_rhombus(n):
    for i in range(n):
        print(generate_line(i, n))

    for i in range(n - 2, -1, -1):
        print(generate_line(i, n))


print_rhombus(int(input()))