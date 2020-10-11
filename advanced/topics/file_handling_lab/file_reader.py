def calculate_sum_with_loop(file_path):
    file = open(file_path, 'r')
    result = 0

    for number_str in file:
        result += int(number_str)
    return result


path = 'numbers.txt'
print(calculate_sum_with_loop(path))