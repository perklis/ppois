import unittest
from client.HistoryOfOrders import HistoryOfOrders
from exceptions import OrderNotFound


class Order:
    def __init__(self, price):
        self.price = price

    def get_total_price(self):
        return self.price


class TestHistoryOfOrders(unittest.TestCase):
    def setUp(self):
        self.history = HistoryOfOrders("Olya")
        self.order1 = Order(10.0)
        self.order2 = Order(200)

    def test_add_and_get_orders(self):
        self.history.add_order(self.order1)
        self.history.add_order(self.order2)
        orders = self.history.get_all_orders()
        self.assertEqual(len(orders), 2)
        self.assertIn(self.order1, orders)
        self.assertIn(self.order2, orders)

    def test_get_last_order(self):
        self.history.add_order(self.order1)
        self.history.add_order(self.order2)
        last_order = self.history.get_last_order()
        self.assertEqual(last_order, self.order2)

    def test_empty_order(self):
        with self.assertRaises(OrderNotFound):
            self.history.get_last_order()

    def test_count_orders(self):
        self.assertEqual(self.history.count_orders(), 0)
        self.history.add_order(self.order1)
        self.assertEqual(self.history.count_orders(), 1)
        self.history.add_order(self.order2)
        self.assertEqual(self.history.count_orders(), 2)

    def test_get_total(self):
        self.history.add_order(self.order1)
        self.history.add_order(self.order2)
        price = self.history.get_total_spent()
        self.assertEqual(price, 210)
