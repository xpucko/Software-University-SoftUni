def check(string):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = []
    for ch in string:
        if ch in open_list:
            stack.append(ch)
        elif ch in close_list:
            pos = close_list.index(ch)
            if len(stack) > 0 and open_list[pos] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return 'NO'
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


print(check(input()))
