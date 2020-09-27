def return_list_abs_values(data):
    return [abs(float(x)) for x in data.split()]


print(return_list_abs_values(input()))