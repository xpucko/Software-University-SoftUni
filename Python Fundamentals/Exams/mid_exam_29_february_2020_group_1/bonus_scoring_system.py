from math import ceil

students = int(input())
lectures = int(input())
bonus = int(input())

total_bonus = 0
attendances = 0
for student in range(students):
    student_attendances = int(input())
    current = student_attendances / lectures * (5 + bonus)
    if current > total_bonus:
        total_bonus = current
        attendances = student_attendances

print(f'Max Bonus: {ceil(total_bonus)}.')
print(f'The student has attended {attendances} lectures.')
