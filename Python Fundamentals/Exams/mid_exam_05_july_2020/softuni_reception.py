questions_per_hour = int(input()) + int(input()) + int(input())
students = int(input())
time = 0

while students > 0:
    time += 1
    if time % 4 == 0:
        time += 1
    students -= questions_per_hour

print(f'Time needed: {time}h.')