import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()
        self.newbie = Beginner('Lion')
        self.pro = Advanced('Juggernaut')
        self.card = MagicCard('Javelin')

    def test_init_valid_arguments(self):
        self.assertEqual(self.controller.player_repository.__class__.__name__, 'PlayerRepository')
        self.assertEqual(self.controller.card_repository.__class__.__name__, 'CardRepository')
        self.assertEqual(self.controller.player_repository.count, 0)
        self.assertEqual(self.controller.card_repository.count, 0)

    def test_add_player_when_player_is_beginner_should_add_it_and_return_a_message(self):
        expected = self.controller.add_player('Beginner', 'Lion')
        self.assertEqual(self.controller.player_repository.count, 1)
        self.assertEqual(len(self.controller.player_repository.players), 1)
        self.assertEqual(expected, "Successfully added player of type Beginner with username: Lion")

    def test_add_player_when_player_is_advanced_should_add_it_and_return_a_message(self):
        expected = self.controller.add_player('Advanced', 'Pudge')
        self.assertEqual(self.controller.player_repository.count, 1)
        self.assertEqual(len(self.controller.player_repository.players), 1)
        self.assertEqual(expected, "Successfully added player of type Advanced with username: Pudge")

    def test_add_card_when_card_is_magic_should_add_it_and_return_a_message(self):
        expected = self.controller.add_card('Magic', 'Javelin')
        self.assertEqual(self.controller.card_repository.count, 1)
        self.assertEqual(len(self.controller.card_repository.cards), 1)
        self.assertEqual(expected, "Successfully added card of type MagicCard with name: Javelin")

    def test_add_card_when_card_is_trap_should_add_it_and_return_a_message(self):
        self.assertEqual(self.controller.card_repository.count, 1)
        self.assertEqual(len(self.controller.card_repository.cards), 1)
        actual = self.controller.add_card('Trap', 'Dagon')
        expected = 'Successfully added card of type TrapCard with name: Dagon'
        self.assertEqual(actual, expected)

    def test_add_player_card_should_add_the_card_to_the_players_repo_and_return_a_message(self):
        self.controller.player_repository.add(self.newbie)
        self.controller.card_repository.add(self.card)
        actual = self.controller.add_player_card('Lion', 'Javelin')
        expected = 'Successfully added card: Javelin to user: Lion'
        self.assertEqual(actual, expected)

    def test_fight_should_return_a_message_with_updated_players_health(self):
        self.controller.player_repository.add(self.newbie)
        self.controller.player_repository.add(self.pro)
        battle_field = BattleField()
        battle_field.fight(self.newbie, self.pro)
        actual = self.controller.fight(self.newbie.username, self.pro.username)
        expected = 'Attack user health 130 - Enemy user health 250'
        self.assertEqual(actual, expected)

    def test_report_should_return_valid_string_representation(self):
        self.controller.player_repository.add(self.newbie)
        self.controller.card_repository.add(self.card)
        self.controller.add_player_card('Lion', 'Javelin')
        expected = 'Username: Lion - Health: 50 - Cards 1\n### Card: Javelin - Damage: 5\n'
        actual = self.controller.report()
        self.assertEqual(expected, actual)
