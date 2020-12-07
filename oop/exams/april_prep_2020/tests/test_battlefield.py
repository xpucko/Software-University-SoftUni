import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self):
        self.battlefield = BattleField()
        self.attacker = Beginner('Juggernaut')
        self.enemy = Advanced('Lion')
        self.card = MagicCard('Demon Edge')

    def test_fight_when_attacker_is_dead_should_raise_error(self):
        self.attacker.health = 0
        with self.assertRaises(ValueError) as content:
            self.battlefield.fight(self.attacker, self.enemy)
        self.assertEqual(str(content.exception), 'Player is dead!')

    def test_fight_when_enemy_is_dead_should_raise_error(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as content:
            self.battlefield.fight(self.attacker, self.enemy)
        self.assertEqual(str(content.exception), 'Player is dead!')

    def test_fight_when_attacker_is_beginner_should_increase_health_and_damage(self):
        self.attacker.card_repository.add(self.card)
        self.battlefield.fight(self.attacker, self.enemy)
        self.assertEqual(self.attacker.health, 170)
        self.assertEqual(self.card.damage_points, 35)

    def test_fight_when_enemy_is_beginner_should_increase_health_and_damage(self):
        self.attacker, self.enemy = self.enemy, self.attacker
        self.enemy.card_repository.add(self.card)
        self.battlefield.fight(self.attacker, self.enemy)
        self.assertEqual(self.enemy.health, 170)
        self.assertEqual(self.card.damage_points, 35)

    def test_fight_should_decrease_players_health(self):
        self.attacker.card_repository.add(self.card)
        self.battlefield.fight(self.attacker, self.enemy)
        self.assertEqual(self.attacker.health, 170)
        self.assertEqual(self.enemy.health, 215)
        self.assertEqual(self.card.damage_points, 35)
