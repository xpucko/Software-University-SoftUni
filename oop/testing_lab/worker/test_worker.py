import unittest


class WorkerTests(unittest.TestCase):
    def test_init_whenCorrectNameSalaryAndEnergy_shouldBeInitialized(self):
        name = 'Test User'
        salary = 1000
        energy = 7
        worker = Worker(name, salary, energy)

        self.assertEqual(worker.name, name)
        self.assertEqual(worker.salary, salary)
        self.assertEqual(worker.energy, energy)
        self.assertEqual(worker.money, 0)

    def test_rest_shouldIncrementEnergy(self):
        name = 'Test User'
        salary = 1000
        energy = 7
        worker = Worker(name, salary, energy)
        worker.rest()
        self.assertEqual(worker.energy, energy + 1)

    def test_work_whenEnergyIs0_shouldRaiseException(self):
        name = 'Test User'
        salary = 1000
        energy = 0
        worker = Worker(name, salary, energy)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertIsNotNone(context.exception)

    def test_work_whenEnergyIsGreaterThan0_shouldIncreaseMoneyBySalary(self):
        name = 'Test User'
        salary = 1000
        energy = 7
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(worker.money, worker.salary)
        worker.work()
        self.assertEqual(worker.money, worker.salary * 2)

    def test_work_shouldDecrementEnergy(self):
        name = 'Test User'
        salary = 1000
        energy = 7
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(worker.energy, energy - 1)

    def test_getInfo_shouldReturnCorrectResult(self):
        name = 'Test User'
        salary = 1000
        energy = 7
        worker = Worker(name, salary, energy)
        expected = f'{name} has saved 0 money.'
        actual = worker.get_info()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
