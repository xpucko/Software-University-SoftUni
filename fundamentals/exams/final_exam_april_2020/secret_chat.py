messages = input()
while True:
    command = input().split(":|:")
    if command[0] == "Reveal":
        print(f"You have a new text message: {messages}")
        break
    elif command[0] == "InsertSpace":
        messages = messages[:int(command[1])] + ' ' + messages[int(command[1]):]
        print(messages)
    elif command[0] == "Reverse":
        substring = command[1]
        if substring in messages:
            messages = messages.replace(substring, '', 1)
            messages += substring[::-1]
            print(messages)
        else:
            print("error")
    elif command[0] == "ChangeAll":
        if command[1] in messages:
            messages = messages.replace(command[1], command[2])
            print(messages)