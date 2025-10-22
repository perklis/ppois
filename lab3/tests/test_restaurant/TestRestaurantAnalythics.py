import unittest
from unittest.mock import Mock
from restaurant.RestaurantAnalytics import RestaurantAnalytics
from orders.Order import Order


class TestRestaurantAnalytics(unittest.TestCase):
    def setUp(self):
        self.analytics = RestaurantAnalytics()
        self.order1 = Mock(spec=Order)
        self.order1.order_number = 1
        self.order1.get_total_price = Mock(return_value=50.0)
        item1 = Mock()
        item1.food_item.name = "Pizza"
        item1.quantity = 2
        item2 = Mock()
        item2.food_item.name = "Burger"
        item2.quantity = 1
        self.order1.items = [item1, item2]

        self.order2 = Mock(spec=Order)
        self.order2.order_number = 2
        self.order2.get_total_price = Mock(return_value=30.0)
        item3 = Mock()
        item3.food_item.name = "Pizza"
        item3.quantity = 1
        item4 = Mock()
        item4.food_item.name = "Salad"
        item4.quantity = 2
        self.order2.items = [item3, item4]

    def test_record_order(self):
        self.analytics.record_order(self.order1)
        self.assertIn(self.order1, self.analytics.orders)

    def test_total_revenue(self):
        self.analytics.record_order(self.order1)
        self.analytics.record_order(self.order2)
        self.assertEqual(self.analytics.total_revenue(), 80.0)

    def test_most_popular_dishes(self):
        self.analytics.record_order(self.order1)
        self.analytics.record_order(self.order2)
        popular = self.analytics.most_popular_dishes()
        self.assertEqual(popular, {"Pizza": 3, "Salad": 2, "Burger": 1})
