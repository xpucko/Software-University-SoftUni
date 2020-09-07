skill = input()
while True:
    line = input()
    if line == 'For Azeroth':
        break
    command = line.split()
    if command[0] == 'GladiatorStance':
        for i in range(len(skill)):
            if skill[i:i + 1].isalpha():
                skill = skill[:i] + skill[i:i + 1].upper() + skill[i + 1:]
        print(skill)
    elif command[0] == 'DefensiveStance':
        for i in range(len(skill)):
            if skill[i:i + 1].isalpha():
                skill = skill[:i] + skill[i:i + 1].lower() + skill[i + 1:]
        print(skill)
    elif command[0] == 'Dispel':
        if int(command[1]) in range(len(skill)):
            skill = skill[: int(command[1])] + command[2] + skill[int(command[1]) + 1:]
            print('Success!')
        else:
            print('Dispel too weak.')
    elif command[0] == 'Target':
        substring = command[2]
        if substring not in skill:
            print("Command doesn't exist!")
        else:
            if command[1] == 'Remove':
                skill = skill.replace(substring, '')
            else:
                skill = skill.replace(substring, command[3])
            print(skill)