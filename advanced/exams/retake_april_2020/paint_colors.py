string = input().split()
main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']
colors_found = []

while string:
    if len(string) == 1:
        if string[0] in main_colors + secondary_colors:
            colors_found.append(string[0])
            string.pop(0)
        else:
            break
    else:
        str_1 = string[0]
        str_2 = string[-1]
        if str_1 + str_2 in main_colors + secondary_colors:
            string.pop(0)
            string.pop(-1)
            colors_found.append(str_1 + str_2)

        elif str_2 + str_1 in main_colors + secondary_colors:
            string.pop(0)
            string.pop(-1)
            colors_found.append(str_2 + str_1)

        else:
            index = len(string) // 2
            str_1 = str_1[:-1]
            str_2 = str_2[:-1]
            if len(str_1) > 0:
                string.insert(index, str_1)
            if len(str_2) > 0:
                string.insert(index, str_2)
            string.pop(0)
            string.pop(-1)

result = []
for color in colors_found:
    if color in secondary_colors:
        if color == 'orange' and 'red' in colors_found and 'yellow' in colors_found:
            result.append(color)
        if color == 'purple' and 'red' in colors_found and 'blue' in colors_found:
            result.append(color)
        if color == 'green' and 'yellow' in colors_found and 'blue' in colors_found:
            result.append(color)
    else:
        result.append(color)

print(result)
