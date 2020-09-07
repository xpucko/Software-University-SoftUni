import re

pattern = r'U\$([A-Z][a-z]{2,})U\$P@\$([a-z]{5,}[\d]{1,})P@\$'
count = 0
for _ in range(int(input())):
    matched = re.findall(pattern, input())
    if not matched:
        print('Invalid username or password')
    else:
        print('Registration was successful')
        print(f'Username: {matched[0][0]}, Password: {matched[0][1]}')
        count += 1
print(f'Successful registrations: {count}')
