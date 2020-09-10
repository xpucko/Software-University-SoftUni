contacts = {}
while True:
    data = input()
    if data.isdigit():
        for _ in range(int(data)):
            contact = input()
            if contact not in contacts:
                print(f'Contact {contact} does not exist.')
            else:
                print(f'{contact} -> {contacts[contact]}')
        break
    name, number = data.split('-')
    contacts[name] = number
