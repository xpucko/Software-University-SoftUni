def get_empty_dict():
    return {category: {} for category in input().split(', ')}


def store_info_in_bunker(bunker):
    for _ in range(int(input())):
        type_item, item, tokens = input().split(' - ')
        item_info = tokens.split(';')
        quantity = int(item_info[0].split(':')[1])
        quality = int(item_info[1].split(':')[1])
        if type_item in bunker:
            bunker[type_item][item] = {'quantity': quantity, 'quality': quality}


def print_bunker_info(bunker):
    count_items = sum([bunker[category][item]['quantity'] for category in bunker for item in bunker[category]])
    avg_quality = sum([bunker[cat][item]['quality'] for cat in bunker for item in bunker[cat]]) / len(bunker)

    print(f'Count of items: {count_items}')
    print(f'Average quality: {avg_quality:.2f}')
    [print(f'{category} -> {", ".join(bunker[category].keys())}') for category in bunker]


my_bunker = get_empty_dict()
store_info_in_bunker(my_bunker)
print_bunker_info(my_bunker)