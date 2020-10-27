import unittest


class TestIntegerList(unittest.TestCase):
    def test_init_whenNotOnlyIntegers_raiseException(self):
        with self.assertRaises(Exception) as context:
            IntegerList(1, '2', 3, True, 5)

        self.assertIsNotNone(context.exception)

    def test_init_whenOnlyIntegers_shouldStoreThem(self):
        values = [1, 2, 3, 4, 5]
        integers = IntegerList(*values)

        self.assertListEqual(values, integers.get_data())

    def test_add_whenValueIsInteger_shouldBeAdded(self):
        integers = IntegerList()
        integers.add(1)

        self.assertListEqual([1], integers.get_data())

    def test_add_whenValueNotInteger_shouldRaise(self):
        integers = IntegerList()

        with self.assertRaises(Exception) as context:
            integers.add({})

        self.assertIsNotNone(context.exception)

    def test_removeIndex_whenIndexIsValid_shouldRemoveElementAndReturnIt(self):
        integers = IntegerList(1, 2, 3, 4, 5, 6, 7)
        returned = integers.remove_index(3)

        self.assertListEqual([1, 2, 3, 5, 6, 7], integers.get_data())
        self.assertEqual(4, returned)

    def test_removeIndex_whenIndexIsInvalid_shouldRaise(self):
        integers = IntegerList(1, 2, 3, 4, 5, 6, 7)

        with self.assertRaises(Exception) as context:
            integers.remove_index(len(integers.get_data()))

        self.assertIsNotNone(context.exception)

    def test_get_whenIndexIsValid_shouldReturnIt(self):
        integers = IntegerList(1, 2, 3, 4, 5, 6, 7)
        returned = integers.get(3)

        self.assertEqual(4, returned)

    def test_get_whenIndexIsInvalid_shouldRaise(self):
        integers = IntegerList(1, 2, 3, 4, 5, 6, 7)

        with self.assertRaises(Exception) as context:
            integers.get(len(integers.get_data()))

        self.assertIsNotNone(context.exception)

    def test_getBiggest_shouldReturnTheMaxElement(self):
        integers = IntegerList(1, 2, 3, 4, 5, 6, 7)
        returned = integers.get_biggest()

        self.assertEqual(7, returned)

    def test_getIndex_shouldReturnTheIndex(self):
        integers = IntegerList(1, 2, 3, 4, 5, 6, 7)
        returned = integers.get_index(4)

        self.assertEqual(3, returned)

    def test_insert_whenIndexIsValid_shouldInsertIt(self):
        integers = IntegerList(1, 2, 3, 4, 5, 6, 7)
        integers.insert(2, -1)

        self.assertListEqual([1, 2, -1, 3, 4, 5, 6, 7], integers.get_data())

    def test_insert_whenIndexIsInvalid_shouldRaise(self):
        integers = IntegerList(1, 2, 3, 4, 5, 6, 7)

        with self.assertRaises(Exception) as context:
            integers.insert(len(integers.get_data()), -1)

        self.assertIsNotNone(context.exception)

    def test_insert_whenValueIsNotInteger_shouldRaise(self):
        integers = IntegerList(1, 2, 3, 4, 5, 6, 7)

        with self.assertRaises(Exception) as context:
            integers.insert(0, True)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
