import unittest
from orders.Order import Order
from orders.OrderItem import OrderItem
from orders.OrderStatus import OrderStatus
from client.Client import Client
from client.Addres import Addres
from restaurant.FoodItem import FoodItem


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.address = Addres("Lenina", "10", "Minsk")
        self.client = Client("Anna", "123456789", self.address)

        self.dish1 = FoodItem("Pizza", 10.0, "Main", 300)
        self.dish2 = FoodItem("Pasta", 15.0, "Main", 400)

        self.order_item1 = OrderItem(self.dish1, 2)
        self.order_item2 = OrderItem(self.dish2, 1)

    def test_add_and_remove_item(self):
        order = Order(self.client)
        order.add_item(self.order_item1)
        order.add_item(self.order_item2)

        self.assertIn(self.order_item1, order.items)
        self.assertIn(self.order_item2, order.items)

        order.remove_item("Pizza")
        self.assertNotIn(self.order_item1, order.items)
        self.assertIn(self.order_item2, order.items)

    def test_get_total_price(self):
        order = Order(self.client)
        order.add_item(self.order_item1)
        order.add_item(self.order_item2)
        self.assertEqual(order.get_total_price(), 35.0)

    def test_change_status_and_delivered_at(self):
        order = Order(self.client)
        order.change_status(OrderStatus.DELIVERED)
        self.assertEqual(order.status, OrderStatus.DELIVERED)
        self.assertIsNotNone(order.delivered_at)

    def test_pay_order(self):
        order = Order(self.client)
        order.add_item(self.order_item1)
        payment = order.pay()
        self.assertIsNotNone(payment)
        self.assertEqual(order.status, OrderStatus.READY)

    def test_show_order(self):
        order = Order(self.client)
        order.add_item(self.order_item1)
        order.show_order()
