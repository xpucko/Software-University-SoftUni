def is_valid_name(name):
    if name[0:1].isupper():
        for ch in name[1:]:
            if not ch.islower() and ch not in [' ', "'"]:
                return False
        return name


def is_valid_song(song):
    for ch in song:
        if not ch.isupper() and ch != ' ':
            return False
    return song


def encrypt_string(string):
    string = [x for x in string]
    key = len(artist)
    for i in range(len(string)):
        if string[i] not in [' ', ':', "'"]:
            if string[i].islower():
                if ord(string[i]) + key in range(97, 123):
                    string[i] = chr(ord(string[i]) + key)
                else:
                    string[i] = chr(ord(string[i]) + key - 26)
            else:
                if ord(string[i]) + key in range(65, 91):
                    string[i] = chr(ord(string[i]) + key)
                else:
                    string[i] = chr(ord(string[i]) + key - 26)
    return "".join(string)


while True:
    line = input()
    if line == 'end':
        break
    artist, title = line.split(':')
    if is_valid_name(artist) and is_valid_song(title):
        print(f'Successful encryption: {encrypt_string(artist)}@{encrypt_string(title)}')
    else:
        print('Invalid input!')