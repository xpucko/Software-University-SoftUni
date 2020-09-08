def find_first_possible_position(stops):
    start = 0
    deficit = 0

    for stop in range(stops):
        petrol, distance = input().split()
        deficit += int(petrol) - int(distance)
        if deficit < 0:
            start = stop + 1
            deficit = 0
    if deficit >= 0:
        return start


print(find_first_possible_position(int(input())))