import unittest

from project.card.trap_card import TrapCard


class TestAdvanced(unittest.TestCase):
    def test_init_when_valid_arguments(self):
        p = TrapCard('Dagon')
        self.assertEqual(p.name, 'Dagon')
        self.assertEqual(p.damage_points, 120)
        self.assertEqual(p.health_points, 5)
