import unittest

from project.player.beginner import Beginner


class TestAdvanced(unittest.TestCase):
    def test_init_when_valid_arguments(self):
        p = Beginner('Crystal Maiden')
        self.assertEqual(p.username, 'Crystal Maiden')
        self.assertEqual(p.health, 50)
