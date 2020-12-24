def get_array(x):
    arr = [0 for _ in range(x)]
    generate_and_print_vector(arr, 0)


def generate_and_print_vector(arr, index):
    if len(arr) <= index:
        print(*arr)
        return

    for i in range(2):
        arr[index] = i
        generate_and_print_vector(arr, index + 1)


n = int(input())
get_array(n)
