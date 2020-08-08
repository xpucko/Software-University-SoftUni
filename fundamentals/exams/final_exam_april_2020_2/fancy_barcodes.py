import re

pattern = r'@[#]+([A-Z][a-zA-Z0-9]{4,}[A-Z])@[#]+'
for _ in range(int(input())):
    line = input()
    matched = re.findall(pattern, line)
    if not matched:
        print('Invalid barcode')
    else:
        result = [ch for ch in matched[0] if ch.isdigit()]
        if not result:
            print('Product group: 00')
        else:
            print(f'Product group: {"".join(result)}')