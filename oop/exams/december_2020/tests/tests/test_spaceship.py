import unittest

from project.spaceship.spaceship import Spaceship


class TestSpaceship(unittest.TestCase):
    def setUp(self):
        self.spaceship = Spaceship('SpaceX', 2)

    def test_init_with_valid_arguments_should_implement_spaceship(self):
        self.assertEqual(self.spaceship.name, 'SpaceX')
        self.assertEqual(self.spaceship.capacity, 2)
        self.assertEqual(self.spaceship.astronauts, [])

    def test_add_when_spaceship_is_full_should_raise_an_error(self):
        self.spaceship.astronauts.append('Tesla')
        self.spaceship.astronauts.append('Elon')
        with self.assertRaises(ValueError) as ex:
            self.spaceship.add('Newton')
        self.assertEqual(str(ex.exception), 'Spaceship is full')

    def test_add_when_astronaut_is_already_in_spaceship_should_raise_an_error(self):
        self.spaceship.astronauts.append('Tesla')
        with self.assertRaises(ValueError) as ex:
            self.spaceship.add('Tesla')
        self.assertEqual(str(ex.exception), 'Astronaut Tesla Exists')

    def test_add_should_append_astronaut_to_spaceship(self):
        self.spaceship.add('Tesla')
        self.assertEqual(self.spaceship.astronauts, ['Tesla'])

    def test_remove_when_non_existent_astronaut_should_raise_an_error(self):
        with self.assertRaises(ValueError) as ex:
            self.spaceship.remove('Elon')
        self.assertEqual(str(ex.exception), 'Astronaut Not Found')

    def test_remove_should_remove_an_astronaut(self):
        self.spaceship.astronauts.append('Elon')
        self.spaceship.remove('Elon')
        self.assertEqual(self.spaceship.astronauts, [])
