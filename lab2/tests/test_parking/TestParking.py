import unittest
from parking.Parking import Parking
from parking.Car import Car
from exceptions import NoFreeSpotError, CarNotFoundError


class TestParking(unittest.TestCase):
    def setUp(self):
        self.parking = Parking("Central Lot", 3)

        self.car1 = Car("Employee", "Alice", "Red", "A123")
        self.car2 = Car("Visitor", "Bob", "Blue", "B456")
        self.car3 = Car("Employee", "Charlie", "Green", "C789")
        self.car4 = Car("Visitor", "David", "Black", "D000")

    def test_park_and_remove_car(self):
        spot1 = self.parking.park_car(self.car1)
        spot2 = self.parking.park_car(self.car2)
        self.assertIn(spot1, [1, 2, 3])
        self.assertIn(spot2, [1, 2, 3])
        self.assertEqual(len(self.parking.occupied_spots), 2)

        self.parking.remove_car(spot1)
        self.assertNotIn(spot1, self.parking.occupied_spots)

    def test_get_free_spots(self):
        self.parking.park_car(self.car1)
        self.parking.park_car(self.car2)
        free = self.parking.get_free_spots()
        self.assertEqual(len(free), 1)

    def test_no_free_spots_error(self):
        self.parking.park_car(self.car1)
        self.parking.park_car(self.car2)
        self.parking.park_car(self.car3)
        with self.assertRaises(NoFreeSpotError):
            self.parking.park_car(self.car4)

    def test_car_not_found_error(self):
        with self.assertRaises(CarNotFoundError):
            self.parking.remove_car(5)
