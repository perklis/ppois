import unittest
from unittest.mock import Mock
from delivery.courier.Courier import Courier
from exceptions import OrderNotFound


class TestCourier(unittest.TestCase):
    def setUp(self):
        self.courier = Courier("Olya", "123", 100)
        self.mock_order = Mock()
        self.mock_item = Mock()
        self.mock_item.food_item.name = "Pasta"
        self.mock_item.order = self.mock_order
        self.order_items = [self.mock_item]

    def test_take_order(self):
        self.courier.take_order(self.order_items)
        self.assertEqual(self.courier.status, "delivering")
        self.assertEqual(self.courier.current_order, self.order_items)

    def test_check_order_status(self):
        self.courier.take_order(self.order_items)
        self.courier.check_order_status()

    def test_check_order_status_no_order(self):
        with self.assertRaises(OrderNotFound):
            self.courier.check_order_status()

    def test_with_rating(self):
        self.courier.take_order(self.order_items)
        old_salary = self.courier.salary
        self.courier.rating.add_rating = Mock()
        self.courier.deliver_order("Bedy", customer_rating=4.5)
        self.assertEqual(self.courier.status, "waiting")
        self.assertIsNone(self.courier.current_order)
        self.assertIn(self.mock_order, self.courier.order_list)
        self.assertAlmostEqual(self.courier.salary, old_salary + 5)
        self.courier.rating.add_rating.assert_called_once_with(self.mock_order, 4.5)

    def test_deliver_success(self):
        self.courier.take_order(self.order_items)
        old_salary = self.courier.salary
        self.courier.deliver_order("Bedy")
        self.assertEqual(self.courier.status, "waiting")
        self.assertAlmostEqual(self.courier.salary, old_salary + 5)

    def test_deliver_order(self):
        with self.assertRaises(OrderNotFound):
            self.courier.deliver_order("Bedy")
