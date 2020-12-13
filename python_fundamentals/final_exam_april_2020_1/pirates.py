def add_city(city: str, population: int, gold: int):
    if city not in data:
        data[city] = [0, 0]
    data[city][0] += population
    data[city][1] += gold


def plunder_city(city, people, gold):
    print(f'{city} plundered! {gold} gold stolen, {people} citizens killed.')
    data[city][0] -= people
    data[city][1] -= gold
    if data[city][0] == 0 or data[city][1] == 0:
        del data[city]
        print(f'{city} has been wiped off the map!')


def prosper_city(city, gold):
    if gold > 0:
        data[city][1] += gold
        print(f'{gold} gold added to the city treasury. {city} now has {data[city][1]} gold.')
    else:
        print('Gold added cannot be a negative number!')


def print_data(data_info):
    if not data_info:
        print('Ahoy, Captain! All targets have been plundered and destroyed')
    else:
        print(f'Ahoy, Captain! There are {len(data_info)} wealthy settlements to go to:')
        for k, v in sorted(data_info.items(), key=lambda x: (-x[1][1], x[0])):
            print(f'{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg')


data = {}
while True:
    line = input().split('||')
    if line[0] == 'Sail':
        break
    add_city(line[0], int(line[1]), int(line[2]))

while True:
    line = input().split('=>')
    if line[0] == 'End':
        print_data(data)
        break
    town = line[1]
    if line[0] == 'Plunder':
        plunder_city(town, int(line[2]), int(line[3]))
    else:
        prosper_city(town, int(line[2]))
