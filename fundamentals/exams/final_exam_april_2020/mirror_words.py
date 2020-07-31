import re

pattern = r'([@]|[#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1'
data = input()
matched = re.findall(pattern, data)
x = []
[x.append(f'{matched[i][1]} <=> {matched[i][2]}') for i in range(len(matched)) if matched[i][1] == matched[i][2][::-1]]
print(f'{len(matched)} word pairs found!') if matched else print('No word pairs found!')
print(f"The mirror words are:\n{', '.join(x)}") if x else print('No mirror words!')
