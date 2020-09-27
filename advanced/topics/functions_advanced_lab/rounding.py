def return_list_round_values(data):
    return [round(float(x)) for x in data.split()]


print(return_list_round_values(input()))