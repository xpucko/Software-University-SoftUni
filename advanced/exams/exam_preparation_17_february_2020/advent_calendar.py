def fix_calendar(args):
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i in range(len(args) - 1):
            if args[i] > args[i + 1]:
                args[i], args[i + 1] = args[i + 1], args[i]
                is_swapped = True

    if not is_swapped:
        return args
