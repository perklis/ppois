import unittest
from unittest.mock import Mock
from restaurant.RestaurantAdministrator import RestaurantAdministrator


class TestRestaurantAdministrator(unittest.TestCase):
    def setUp(self):
        self.admin = RestaurantAdministrator("Olga")
        self.client = Mock()
        self.client.name = "Alice"
        self.client.loyalty_card = Mock()
        self.order = Mock()
        self.order.price = 100.0

    def test_confirm_delivery_applies_cashback(self):
        self.admin.confirm_delivery(self.client, self.order)
        self.client.loyalty_card.add_cashback.assert_called_once_with(self.order.price)
        delivered_orders = self.admin.get_all_delivered_orders()
        self.assertIn(self.order, delivered_orders)

    def test_get_all_delivered_orders_empty_initially(self):
        self.assertEqual(self.admin.get_all_delivered_orders(), [])
