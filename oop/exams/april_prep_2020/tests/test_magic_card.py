import unittest

from project.card.magic_card import MagicCard


class TestAdvanced(unittest.TestCase):
    def setUp(self):
        self.c = MagicCard('Battle Fury')

    def test_init_when_valid_arguments(self):
        self.assertEqual(self.c.name, 'Battle Fury')
        self.assertEqual(self.c.damage_points, 5)
        self.assertEqual(self.c.health_points, 80)

    def test_name_when_is_empty_string_should_raise_error(self):
        with self.assertRaises(ValueError) as content:
            self.c.name = ''
        self.assertEqual(str(content.exception), "Card's name cannot be an empty string.")

    def test_damage_points_when_is_negative_should_raise_error(self):
        with self.assertRaises(ValueError) as content:
            self.c.damage_points = -1
        self.assertEqual(str(content.exception), "Card's damage points cannot be less than zero.")

    def test_health_points_when_is_negative_should_raise_error(self):
        with self.assertRaises(ValueError) as content:
            self.c.health_points = -1
        self.assertEqual(str(content.exception), "Card's HP cannot be less than zero.")
