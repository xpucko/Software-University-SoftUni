data = {}
for _ in range(int(input())):
    student, grade = input().split()
    if student not in data:
        data[student] = []
    data[student].append(float(grade))

for name, grades in data.items():
    grades_str = ' '.join(f'{grade:.2f}' for grade in grades)
    print(f'{name} -> {grades_str} (avg: {sum(grades) / len(grades):.2f})')