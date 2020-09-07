cards = input().split(':')
deck = []
while True:
    data = input().split()
    if data[0] == 'Ready':
        print(*deck)
        break
    command, card = data[0], data[1]
    if command == 'Add':
        deck.append(card) if card in cards else print('Card not found.')
    elif command == 'Insert':
        index = int(data[2])
        deck.insert(index, card) if index in range(len(deck)) and card in cards else print('Error!')
    elif command == 'Remove':
        deck.remove(card) if card in deck else print('Card not found.')
    elif command == 'Swap':
        index_1, index_2 = deck.index(data[1]), deck.index(data[2])
        deck[index_1], deck[index_2] = deck[index_2], deck[index_1]
    elif command == 'Shuffle':
        deck.reverse()