cars = {}
for i in range(int(input())):
    car, car_mileage, car_fuel = input().split('|')
    cars[car] = [int(car_mileage), int(car_fuel)]
while True:
    line = input().split(' : ')
    if line[0] == 'Stop':
        for k, v in sorted(cars.items(), key=lambda x: (-x[1][0], x[0])):
            print(f'{k} -> Mileage: {v[0]} kms, Fuel in the tank: {v[1]} lt.')
        break
    command, car, data = line[0], line[1], int(line[2])
    if command == 'Drive':
        data_2 = int(line[3])
        if cars[car][1] < data_2:
            print('Not enough fuel to make that ride')
        else:
            cars[car][1] -= data_2
            cars[car][0] += data
            print(f'{car} driven for {data} kilometers. {data_2} liters of fuel consumed.')
        if cars[car][0] >= 100000:
            del cars[car]
            print(f'Time to sell the {car}!')
    elif command == 'Refuel':
        if cars[car][1] + data > 75:
            print(f'{car} refueled with {75 - cars[car][1]} liters')
            cars[car][1] = 75
        else:
            cars[car][1] += data
            print(f'{car} refueled with {data} liters')
    else:
        if cars[car][0] - data < 10000:
            cars[car][0] = 10000
        else:
            cars[car][0] -= data
            print(f'{car} mileage decreased by {data} kilometers')