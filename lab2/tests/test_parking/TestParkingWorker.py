import unittest
from parking.Parking import Parking
from parking.Car import Car
from parking.ParkingWorker import ParkingWorker
from exceptions import NoFreeSpotError


class TestParkingWorker(unittest.TestCase):
    def setUp(self):
        self.parking = Parking("Central Lot", 2)
        self.worker = ParkingWorker("Eve", 30, 5, 2000, self.parking)
        self.car1 = Car("Employee", "Alice", "Red", "A123")
        self.car2 = Car("Visitor", "Bob", "Blue", "B456")

    def test_park_car_worker(self):
        self.worker.park_car(self.car1)
        self.assertIn(self.car1, self.parking.occupied_spots.values())
        self.assertEqual(self.worker._cars_served_today, 1)

    def test_remove_car_worker(self):
        self.worker.park_car(self.car1)
        spot = list(self.parking.occupied_spots.keys())[0]
        self.worker.remove_car(spot)
        self.assertNotIn(spot, self.parking.occupied_spots)
        self.assertIsNone(self.worker._current_car)

    def test_get_free_spots_worker(self):
        self.worker.park_car(self.car1)
        free = self.worker.get_free_spots()
        self.assertEqual(len(free), 1)

    def test_no_free_spots_error_worker(self):
        self.worker.park_car(self.car1)
        self.worker.park_car(self.car2)
        with self.assertRaises(NoFreeSpotError):
            self.worker.get_free_spots()

    def test_reset_cars_served(self):
        self.worker.park_car(self.car1)
        self.worker.park_car(self.car2)
        self.worker.reset_cars_served()
        self.assertEqual(self.worker._cars_served_today, 0)
