import unittest


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car(100, 8)

    def test_carDrive_whenEnoughFuel(self):
        self.car.drive(5)
        self.assertEqual(self.car.fuel_quantity, 55.5)

    def test_carDrive_whenNotEnoughFuel(self):
        self.car.drive(100)
        self.assertEqual(self.car.fuel_quantity, 100)

    def test_carRefuel(self):
        self.car.refuel(5)
        self.assertEqual(self.car.fuel_quantity, 105)


class TestTruck(unittest.TestCase):

    def setUp(self):
        self.truck = Truck(100, 10)

    def test_truckDrive_whenEnoughFuel(self):
        self.truck.drive(3)
        self.assertEqual(self.truck.fuel_quantity, 65.2)

    def test_truckDrive_whenNotEnoughFuel(self):
        self.truck.drive(200)
        self.assertEqual(self.truck.fuel_quantity, 100)

    def test_truckRefuel(self):
        self.truck.refuel(10)
        self.assertEqual(self.truck.fuel_quantity, 109.5)


if __name__ == '__main__':
    unittest.main()
