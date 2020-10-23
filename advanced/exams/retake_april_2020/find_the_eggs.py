def find_strongest_eggs(*args):
    nums, sublist_count = args
    matrix = [[] for _ in range(sublist_count)]
    while nums:
        for i in range(len(matrix)):
            matrix[i].append(nums[0])
            nums.pop(0)

    result = []
    for sublist in matrix:
        left_num = sublist[(len(sublist) // 2) - 1]
        mid_num = sublist[len(sublist) // 2]
        right_num = sublist[(len(sublist) // 2) + 1]
        cond_1 = left_num < mid_num > right_num
        cond_2 = left_num < right_num
        if cond_1 and cond_2:
            result.append(mid_num)

    return result
