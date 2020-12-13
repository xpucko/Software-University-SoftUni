import re

pattern = r'![A-Z][a-z][a-z]+!:[[][A-Za-z]{8,}[]]'
for _ in range(int(input())):
    data = input()
    matches = re.findall(pattern, data)
    print("The message is invalid") if not matches else print(
        f"{matches[0].split(':')[0][1:-1]}: {' '.join(map(str, [ord(ch) for ch in matches[0].split(':')[1][1:-1]]))}")
