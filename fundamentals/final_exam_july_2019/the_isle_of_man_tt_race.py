import re

pattern = r'([#\$%\*&])([A-Za-z]+)(\1)=([\d]+)!!(.*)'
is_found = False
while True:
    data = input()
    matched = re.findall(pattern, data)
    if matched:
        length = int(matched[0][3])
        code = [x for x in matched[0][4]]
        if length == len(code):
            for i in range(length):
                code[i] = chr(ord(code[i]) + length)
            print(f'Coordinates found! {matched[0][1]} -> {"".join(code)}')
            is_found = True
    if not is_found:
        print('Nothing found!')
    else:
        break