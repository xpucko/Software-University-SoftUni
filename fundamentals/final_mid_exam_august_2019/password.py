import re

pattern = r'(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^><]{3})<(\1)'
for _ in range(int(input())):
    match = re.findall(pattern, input())
    print(f'Password: {match[0][1]}{match[0][2]}{match[0][3]}{match[0][4]}') if match else print('Try another password!')