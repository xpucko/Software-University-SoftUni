import unittest

from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room('Daniels', 1000, 2)

    def test_init_when_valid_arguments_should_implement(self):
        self.assertEqual(self.room.family_name, 'Daniels')
        self.assertEqual(self.room.budget, 1000)
        self.assertEqual(self.room.members_count, 2)
        self.assertEqual(self.room.children, [])
        self.assertEqual(self.room.expenses, 0)

    def test_expenses_when_value_is_negative_should_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.room.expenses = -1

        self.assertEqual('Expenses cannot be negative', str(context.exception))
