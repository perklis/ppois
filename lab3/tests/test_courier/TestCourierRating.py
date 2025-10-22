import unittest
from unittest.mock import Mock
from delivery.courier.CourierRating import CourierRating


class TestCourierRating(unittest.TestCase):
    def setUp(self):
        self.mock_courier = Mock()
        self.mock_courier.name = "Rustam"
        self.mock_courier.salary = 100
        self.mock_order = Mock()
        self.mock_order.order_number = 123

        self.rating_system = CourierRating(self.mock_courier)

    def test_add_rating_valid(self):
        self.rating_system.add_rating(self.mock_order, 5)
        self.assertEqual(self.rating_system.ratings, [5])

    def test_add_rating_invalid_low(self):
        with self.assertRaises(Exception):
            self.rating_system.add_rating(self.mock_order, 0)

    def test_add_rating_invalid_high(self):
        with self.assertRaises(Exception):
            self.rating_system.add_rating(self.mock_order, 6)

    def test_average_rating(self):
        self.rating_system.add_rating(self.mock_order, 4)
        self.rating_system.add_rating(self.mock_order, 5)
        self.assertEqual(self.rating_system.get_average_rating(), 4.5)

    def test_bonus_applied(self):
        self.rating_system.add_rating(self.mock_order, 5)
        self.assertEqual(self.mock_courier.salary, 110)

    def test_bonus_not_applied(self):
        self.rating_system.add_rating(self.mock_order, 3)
        self.assertEqual(self.mock_courier.salary, 100)
