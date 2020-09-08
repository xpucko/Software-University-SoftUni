from collections import deque


def solve():
    liters = int(input())
    people = deque()
    while True:
        person = input()
        if person == 'Start':
            break
        people.append(person)

    while people:
        command = input().split()
        if command[0] == 'End':
            break
        elif command[0] == 'refill':
            liters += int(command[1])
        else:
            person = people.popleft()
            person_liters = int(command[0])
            if liters < person_liters:
                print(f'{person} must wait')
            else:
                liters -= person_liters
                print(f'{person} got water')
    print(f'{liters} liters left')


solve()
