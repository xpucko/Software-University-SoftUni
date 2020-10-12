import os

while True:
    input_line = input().split('-')
    if input_line[0] == 'End':
        break

    command, file_name = input_line[0], input_line[1]
    if command == 'Create':
        with open(file_name, 'w') as file:
            file.write('')

    elif command == 'Delete':
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print('An error occurred')

    elif command == 'Add':
        content = input_line[2]
        with open(file_name, 'a') as file:
            file.write(content + '\n')

    elif command == 'Replace':
        if os.path.exists(file_name):
            old_string = input_line[2]
            new_string = input_line[3]
            with open(file_name, 'r') as file:
                file_data = file.read()
            file_data = file_data.replace(old_string, new_string)
            with open(file_name, 'w') as file:
                file.write(file_data)
        else:
            print('An error occurred')