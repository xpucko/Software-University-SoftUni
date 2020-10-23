def numbers_searching(*args):
    sorted_nums = sorted(set(args))
    duplicates = sorted(set(x for x in args if args.count(x) > 1))
    for i in range(len(sorted_nums) - 1):
        if sorted_nums[i] + 1 != sorted_nums[i + 1]:
            return [sorted_nums[i] + 1, duplicates]
