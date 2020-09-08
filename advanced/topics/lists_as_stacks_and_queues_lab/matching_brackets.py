def get_matching_brackets(expression):
    opening_brackets = []
    sub_expressions = []
    for i in range(len(expression)):
        ch = expression[i]
        if ch == '(':
            opening_brackets.append(i)
        elif ch == ')':
            start_index = opening_brackets.pop()
            sub_expressions.append(expression[start_index:i + 1])
    return sub_expressions


[print(x) for x in get_matching_brackets(input())]
