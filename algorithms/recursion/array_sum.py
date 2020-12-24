def get_array_sum(arr, idx):
    if idx == len(arr):
        return 0

    return arr[idx] + get_array_sum(arr, idx + 1)


array = [int(x) for x in input().split()]
print(get_array_sum(array, 0))
