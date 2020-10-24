def list_manipulator(result, command, position, *args):
    if command == 'add':
        if position == 'beginning':
            result = list(args) + list(result)
        else:
            result += list(args)
    elif command == 'remove':
        if args:
            if args[0] > 1:
                for _ in range(args[0]):
                    if position == 'beginning':
                        result.pop(0)
                    else:
                        result.pop()
        else:
            if position == 'beginning':
                result.pop(0)
            else:
                result.pop()

    return result
