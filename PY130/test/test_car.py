from car import Car
import unittest

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Porsche", 1971)

    def test_getter(self):
        #self.assertEqual("Porsche", self.car.name)
        self.assertEqual(Car("Porsche", 1971), self.car)

    def test_true(self):
        self.assertTrue(self.car is not None)

    def test_instance(self):
        self.assertIsInstance(self.car, Car)

    def test_in(self):
        self.assertIn(self.car._year, [1970, 1971])

    def test_exception(self):
        with self.assertRaises('AttributeError'):
            print(self.car.year)

    @unittest.skip
    def test_exception_2(self):
        self.assertEqual(1971, self.car.year)

    @unittest.skip
    def test_failure(self):
        self.assertEqual(1972, self.car._year)
    
if __name__ == "__main__":
    unittest.main()