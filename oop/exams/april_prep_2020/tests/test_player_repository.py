import unittest

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestCardRepository(unittest.TestCase):
    def setUp(self):
        self.rep = PlayerRepository()
        self.player = Beginner('Ursa')

    def test_init_should_initializes(self):
        self.assertEqual(self.rep.count, 0)
        self.assertEqual(self.rep.players, [])

    def test_add_when_player_is_already_in_repository_should_raise_error(self):
        self.rep.players.append(self.player)
        with self.assertRaises(ValueError) as content:
            self.rep.add(self.player)
        self.assertEqual(str(content.exception), 'Player Ursa already exists!')

    def test_add_when_player_is_not_in_the_repository_should_add_it_and_increase_count_by_one(self):
        self.rep.add(self.player)
        self.assertEqual(self.rep.players, [self.player])
        self.assertEqual(self.rep.count, 1)

    def test_remove_when_empty_string_should_raise_error(self):
        incorrect_card = ''
        with self.assertRaises(ValueError) as content:
            self.rep.remove(incorrect_card)
        self.assertEqual(str(content.exception), 'Player cannot be an empty string!')

    def test_remove_when_player_is_valid_should_remove_it_and_decrease_count_by_one(self):
        self.rep.players.append(self.player)
        self.rep.count = 1
        self.rep.remove(self.player.username)
        self.assertEqual(self.rep.players, [])
        self.assertEqual(self.rep.count, 0)

    def test_find_return_searched_player(self):
        self.rep.players.append(self.player)
        self.rep.players.append(Beginner('Razor'))
        self.assertEqual(self.player, self.rep.find('Ursa'))
