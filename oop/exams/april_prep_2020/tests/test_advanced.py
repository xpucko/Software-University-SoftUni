import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    def setUp(self):
        self.p = Advanced('Anti-Mage')

    def test_init_when_valid_arguments(self):
        self.assertEqual(self.p.username, 'Anti-Mage')
        self.assertEqual(self.p.health, 250)

    def test_username_when_is_empty_string_should_raise_error(self):
        with self.assertRaises(ValueError) as content:
            self.p.username = ''
        self.assertEqual(str(content.exception), "Player's username cannot be an empty string.")

    def test_health_when_is_negative_should_raise_error(self):
        with self.assertRaises(ValueError) as content:
            self.p.health = -1
        self.assertEqual(str(content.exception), "Player's health bonus cannot be less than zero.")

    def test_take_damage_when_is_negative_should_raise_error(self):
        with self.assertRaises(ValueError) as content:
            self.p.take_damage(-1)
        self.assertEqual(str(content.exception), "Damage points cannot be less than zero.")

    def test_take_damage_when_is_valid_should_decrease_health(self):
        self.p.take_damage(50)
        self.assertEqual(self.p.health, 200)

    def test_is_dead_when_value_is_zero_should_return_true(self):
        self.p.health = 0
        self.assertTrue(self.p.is_dead)

    def test_is_dead_when_value_is_positive_should_return_false(self):
        self.assertFalse(self.p.is_dead)
