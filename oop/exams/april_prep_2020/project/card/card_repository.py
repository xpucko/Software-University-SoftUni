from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        if any(c.name == card.name for c in self.cards):
            raise ValueError(f'Card {card.name} already exists!')

        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == '':
            raise ValueError('Card cannot be an empty string!')

        self.cards.remove(self.find(card))
        self.count -= 1

    def find(self, name: str):
        return [c for c in self.cards if c.name == name][0]
