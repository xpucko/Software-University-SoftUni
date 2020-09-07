email = input()
while True:
    command = input().split()
    if command[0] == 'Complete':
        break
    elif command[0] == 'Make':
        if command[1] == 'Upper':
            email = email.upper()
            print(email.upper())
        elif command[1] == 'Lower':
            email = email.lower()
            print(email.lower())
    elif command[0] == 'GetDomain':
        print(email[-int(command[1]):])
    elif command[0] == 'GetUsername':
        print(email[:email.index('@')]) if '@' in email else print(f"The email {email} doesn't contain the @ symbol.")
    elif command[0] == 'Replace':
        email = email.replace(command[1], '-')
        print(email)
    elif command[0] == 'Encrypt':
        print(*[ord(ch) for ch in email])