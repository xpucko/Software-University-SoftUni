import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hw = Hardware('Test hw', 'Power', 100, 50)
        self.sw = Software('Test sw', 'Light', 20, 10)

    def test_init_when_valid_arguments_should_implement(self):
        self.assertEqual(self.hw.name, 'Test hw')
        self.assertEqual(self.hw.type, 'Power')
        self.assertEqual(self.hw.capacity, 100)
        self.assertEqual(self.hw.memory, 50)
        self.assertEqual(self.hw.software_components, [])

    def test_install_when_not_enough_memory_or_capacity_should_raise_exception(self):
        self.sw = Software('Test sw', 'Light', 101, 51)
        with self.assertRaises(Exception) as ex:
            self.hw.install(self.sw)
        self.assertEqual(str(ex.exception), 'Software cannot be installed')

    def test_uninstall_when_software_in_components_should_remove_it(self):
        self.hw.software_components.append(self.sw)
        self.hw.uninstall(self.sw)
        self.assertEqual(self.hw.software_components, [])
