with open('text.txt', 'r') as file:
    result = ''
    for index, line in enumerate(file):
        counter_letters = len([x for x in line if x.isalpha()])
        counter_symbols = len([x for x in line if not x.isalpha() and not x.isspace()])
        result += f'Line {index + 1}: {line[:-1]} ({counter_letters})({counter_symbols})\n'

with open('output.txt', 'w') as file:
    file.write(result)