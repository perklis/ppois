import unittest
from orders.Order import Order
from delivery.courier.Courier import Courier
from restaurant.kitchen.OrderQueue import OrderQueue
from exceptions import EmptyOrderQueue
from client.Addres import Addres


class TestOrderQueue(unittest.TestCase):
    def setUp(self):
        self.queue = OrderQueue()
        self.address = Addres("Bedy", "10", "Minsk")
        self.client = type("Client", (), {})()
        self.client.name = "Bunny"
        self.client._address = self.address
        self.order1 = Order(self.client)
        self.order2 = Order(self.client)
        self.courier = Courier("Bobny", "123456", 1000)

    def test_add_and_count_orders(self):
        self.queue.add_order(self.order1)
        self.queue.add_order(self.order2)
        self.assertEqual(self.queue.count(), 2)

    def test_next_order_returns_order_and_assigns_courier(self):
        self.queue.add_order(self.order1)
        order = self.queue.next_order(self.courier)
        self.assertEqual(order, self.order1)
        self.assertEqual(self.queue.count(), 0)

    def test_next_order_without_orders_raises(self):
        with self.assertRaises(EmptyOrderQueue):
            self.queue.next_order()

    def test_list_orders_prints(self):
        self.queue.add_order(self.order1)
        self.queue.add_order(self.order2)
        self.queue.list_orders()
