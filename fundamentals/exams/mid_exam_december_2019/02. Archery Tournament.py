targets = [int(target) for target in input().split("|")]
points = 0
while True:
    line = input()
    if line == "Reverse":
        targets.reverse()
        continue
    elif line == "Game over":
        print(f"{' - '.join([str(target) for target in targets])}")
        print(f"Iskren finished the archery tournament with {points} points!")
        break

    line = line.split(" ")
    traversing = line[1].split("@")
    direction = traversing[0]
    start = int(traversing[1])
    length = int(traversing[2])

    if 0 <= start < len(targets):  # check if startIndex is valid
        if direction == "Left":
            index = start - length
            if index < 0:  # index<0 <=> length>start
                while index < 0:  # adding len(targets) to index till 0<=index<len(targets)
                    index += len(targets)
        else:
            index = start + length
            if index >= len(targets):  # index-valid <=> index<len(targets)
                while index >= len(targets):  # reduce index with len(targets) till 0<=index<len(targets)
                    index -= len(targets)

        if targets[index] >= 5:
            points += 5
            targets[index] -= 5
        else:
            points += targets[index]
            targets[index] = 0