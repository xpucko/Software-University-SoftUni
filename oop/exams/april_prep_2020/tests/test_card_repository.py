import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def setUp(self):
        self.rep = CardRepository()
        self.card = MagicCard('Javelin')

    def test_init_should_initializes(self):
        self.assertEqual(self.rep.count, 0)
        self.assertEqual(self.rep.cards, [])

    def test_add_when_card_is_already_in_repository_should_raise_error(self):
        self.rep.cards.append(self.card)
        with self.assertRaises(ValueError) as content:
            self.rep.add(self.card)
        self.assertEqual(str(content.exception), 'Card Javelin already exists!')

    def test_add_when_card_is_not_in_the_repository_should_add_it_and_increase_count_by_one(self):
        self.rep.add(self.card)
        self.assertEqual(self.rep.cards, [self.card])
        self.assertEqual(self.rep.count, 1)

    def test_remove_when_empty_string_should_raise_error(self):
        incorrect_card = ''
        with self.assertRaises(ValueError) as content:
            self.rep.remove(incorrect_card)
        self.assertEqual(str(content.exception), 'Card cannot be an empty string!')

    def test_remove_when_card_is_valid_should_remove_it_and_decrease_count_by_one(self):
        self.rep.cards.append(self.card)
        self.rep.count = 1
        self.rep.remove(self.card.name)
        self.assertEqual(self.rep.cards, [])
        self.assertEqual(self.rep.count, 0)

    def test_find_return_searched_card(self):
        self.rep.cards.append(self.card)
        self.rep.cards.append(MagicCard('Battle Fury'))
        self.assertEqual(self.card, self.rep.find('Javelin'))
