import unittest


class TestCar(unittest.TestCase):
    def __get_exception_from_init(self, make, model, fuel_consumption, fuel_capacity):
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)
        return context.exception

    def test_init_whenValidValues_shouldInitialize(self):
        make = 'Test make'
        model = 'Test model'
        fuel_consumption = 8
        fuel_capacity = 50

        car = Car(make, model, fuel_consumption, fuel_capacity)
        expected = [make, model, fuel_consumption, fuel_capacity, 0]
        actual = [car.make, car.model, car.fuel_consumption, car.fuel_capacity, car.fuel_amount]

        self.assertEqual(expected, actual)

    def test_init_whenNoneMake_shouldRaiseException(self):
        make = None
        model = 'Test model'
        fuel_consumption = 8
        fuel_capacity = 50

        exception = self.__get_exception_from_init(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(exception)

    def test_init_whenEmptyStringMake_shouldRaiseException(self):
        make = ''
        model = 'Test model'
        fuel_consumption = 8
        fuel_capacity = 50

        exception = self.__get_exception_from_init(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(exception)

    def test_init_whenNoneModel_shouldRaiseException(self):
        make = 'Test make'
        model = None
        fuel_consumption = 8
        fuel_capacity = 50

        exception = self.__get_exception_from_init(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(exception)

    def test_init_whenEmptyStringModel_shouldRaiseException(self):
        make = 'Test make'
        model = ''
        fuel_consumption = 8
        fuel_capacity = 50

        exception = self.__get_exception_from_init(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(exception)

    def test_init_whenNegativeFuelConsumption_shouldRaiseException(self):
        make = 'Test make'
        model = 'Test model'
        fuel_consumption = -1
        fuel_capacity = 50

        exception = self.__get_exception_from_init(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(exception)

    def test_init_whenZeroFuelConsumption_shouldRaiseException(self):
        make = 'Test make'
        model = 'Test model'
        fuel_consumption = 0
        fuel_capacity = 50

        exception = self.__get_exception_from_init(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(exception)

    def test_init_whenNegativeFuelCapacity_shouldRaiseException(self):
        make = 'Test make'
        model = 'Test model'
        fuel_consumption = 8
        fuel_capacity = -1

        exception = self.__get_exception_from_init(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(exception)

    def test_init_whenZeroFuelCapacity_shouldRaiseException(self):
        make = 'Test make'
        model = 'Test model'
        fuel_consumption = 8
        fuel_capacity = 0

        exception = self.__get_exception_from_init(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(exception)

    def test_init_whenNegativeFuelAmount_shouldRaiseException(self):
        make = 'Test make'
        model = 'Test model'
        fuel_consumption = 8
        fuel_capacity = 50

        car = Car(make, model, fuel_consumption, fuel_capacity)

        with self.assertRaises(Exception) as context:
            car.fuel_amount = -1

        self.assertIsNotNone(context.exception)

    def test_refuel_whenNegativeFuel_shouldRaiseException(self):
        make = 'Test make'
        model = 'Test model'
        fuel_consumption = 8
        fuel_capacity = 50

        car = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.refuel(-1)

        self.assertIsNotNone(context.exception)

    def test_refuel_whenZeroFuel_shouldRaiseException(self):
        make = 'Test make'
        model = 'Test model'
        fuel_consumption = 8
        fuel_capacity = 50

        car = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.refuel(0)

        self.assertIsNotNone(context.exception)

    def test_refuel_whenPositiveFuelAndEnoughInCapacity_shouldIncreaseAmount(self):
        make = 'Test make'
        model = 'Test model'
        fuel_consumption = 8
        fuel_capacity = 50

        car = Car(make, model, fuel_consumption, fuel_capacity)
        car.refuel(20)

        self.assertEqual(20, car.fuel_amount)

    def test_refuel_whenPositiveFuelAndMoreThanCapacity_shouldSetAmountToCapacity(self):
        make = 'Test make'
        model = 'Test model'
        fuel_consumption = 8
        fuel_capacity = 50

        car = Car(make, model, fuel_consumption, fuel_capacity)
        car.refuel(car.fuel_capacity * 2)

        self.assertEqual(car.fuel_capacity, car.fuel_amount)

    def test_drive_whenEnoughFuel_shouldDecreaseFuel(self):
        make = 'Test make'
        model = 'Test model'
        fuel_consumption = 8
        fuel_capacity = 50

        car = Car(make, model, fuel_consumption, fuel_capacity)
        car.refuel(car.fuel_capacity)
        distance = 200
        car.drive(distance)
        expected = car.fuel_capacity - car.fuel_consumption * distance / 100
        actual = car.fuel_amount

        self.assertEqual(expected, actual)

    def test_drive_whenNotEnoughFuel_shouldRaiseException(self):
        make = 'Test make'
        model = 'Test model'
        fuel_consumption = 8
        fuel_capacity = 50

        car = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.drive(200)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
