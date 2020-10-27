import unittest


class CatTests(unittest.TestCase):
    def test_eat_shouldIncreaseSizeBy1(self):
        name = 'Meow'
        cat = Cat(name)
        original_size = cat.size

        cat.eat()

        self.assertEqual(cat.size, original_size + 1)

    def test_eat_shouldSetSleepyToTrue(self):
        name = 'Test cat'
        cat = Cat(name)

        cat.eat()

        self.assertTrue(cat.sleepy)

    def test_eat_whenAlreadyFed_shouldRaiseException(self):
        name = 'Test cat'
        cat = Cat(name)

        cat.eat()

        with self.assertRaises(Exception) as context:
            cat.eat()

        self.assertIsNotNone(context.exception)

    def test_sleep_whenNotFed_shouldRaiseException(self):
        name = 'Test cat'
        cat = Cat(name)

        with self.assertRaises(Exception) as context:
            cat.sleep()

        self.assertIsNotNone(context.exception)

    def test_sleep_whenFed_shouldSetSleepyToFalse(self):
        name = 'Test cat'
        cat = Cat(name)

        cat.eat()
        cat.sleep()

        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()
