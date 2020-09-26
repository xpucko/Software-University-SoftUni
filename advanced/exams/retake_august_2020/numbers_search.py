def numbers_searching(*args):
    total_numbers_set = sorted(set(x for x in args))
    duplicates = set(x for x in args if args.count(x) > 1)
    for i in range(len(total_numbers_set) - 1):
        if total_numbers_set[i] + 1 != total_numbers_set[i + 1]:
            return [total_numbers_set[i] + 1, sorted(duplicates)]