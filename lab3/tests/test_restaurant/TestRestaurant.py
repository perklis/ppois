import unittest
from unittest.mock import Mock
from restaurant.Restaurant import Restaurant
from restaurant.kitchen.Cook import Cook
from restaurant.kitchen.Shef import Shef
from restaurant.Picker import Picker
from delivery.courier.Courier import Courier
from orders.Order import Order
from client.Client import Client


class TestRestaurant(unittest.TestCase):
    def setUp(self):
        self.restaurant = Restaurant("Clod Mone")
        self.shef = Shef("Victor", 1000, "123456789")
        self.cook = Cook("Oguzok", 800, "987654321", "Italian")
        self.picker = Picker("Lui", 500, "5555555")

        self.courier = Mock(spec=Courier)
        self.courier.name = "Courier Stas"
        self.courier.status = "waiting"
        self.courier.current_order = None
        self.courier.take_order = Mock()

        self.client = Mock(spec=Client)
        self.client.name = "Client Nastya"

        self.order = Mock(spec=Order)
        self.order.order_number = 1
        self.order.items = []

    def test_add_staff(self):
        self.restaurant.add_shef(self.shef)
        self.assertEqual(self.restaurant.shef, self.shef)

        self.restaurant.add_cook(self.cook)
        self.assertIn(self.cook, self.restaurant.cooks)

        self.restaurant.add_picker(self.picker)
        self.assertIn(self.picker, self.restaurant.pickers)

        self.restaurant.add_courier(self.courier)
        self.assertIn(self.courier, self.restaurant.couriers)

    def test_receive_order(self):
        self.restaurant.receive_order(self.order, self.client)
        self.assertIn(self.order, self.restaurant.queue._queue)

    def test_process_next_order_assigns_to_waiting_courier(self):
        self.restaurant.add_courier(self.courier)
        self.restaurant.receive_order(self.order, self.client)
        next_order = self.restaurant.process_next_order()
        self.assertEqual(next_order, self.order)

    def test_add_rating(self):
        self.restaurant.rating.add_rating = Mock()
        self.restaurant.add_rating(self.order, 4.5)
        self.restaurant.rating.add_rating.assert_called_once_with(self.order, 4.5)
