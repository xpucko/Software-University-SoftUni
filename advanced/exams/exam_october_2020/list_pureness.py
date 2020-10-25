def best_list_pureness(numbers, k):
    count = 0
    best_sum = 0

    for i in range(k + 1):
        current = 0

        for j in range(len(numbers)):
            current += numbers[j] * j

        if current > best_sum:
            best_sum = current
            count = i

        numbers.insert(0, numbers.pop())

    return f'Best pureness {best_sum} after {count} rotations'
