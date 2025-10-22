import unittest
from delivery_support.CallCenter import CallCenter
from client.Client import Client
from client.Addres import Addres
from restaurant.FoodItem import FoodItem
from delivery.DeliveryZone import DeliveryZone
from exceptions import EmptyClientWishlistError


class AlwaysAvailableZone(DeliveryZone):
    def is_in_zone(self, address):
        return True


class TestCallCenter(unittest.TestCase):
    def setUp(self):
        self.call_center = CallCenter("TestCenter")
        self.address = Addres("Lenina", "10", "TestCity")
        self.client = Client("Alice", "123456789", self.address)
        self.dish1 = FoodItem("Pizza", 10.0, "Main", 300)
        self.dish2 = FoodItem("Burger", 8.5, "Main", 250)
        self.client._wishlist = [self.dish1, self.dish2]

        self.original_zone_class = CallCenter.__dict__["take_order"].__globals__[
            "DeliveryZone"
        ]
        CallCenter.__dict__["take_order"].__globals__["DeliveryZone"] = (
            AlwaysAvailableZone
        )

    def tearDown(self):
        CallCenter.__dict__["take_order"].__globals__["DeliveryZone"] = (
            self.original_zone_class
        )

    def test_take_order_success_without_gift_card(self):
        order = self.call_center.take_order(self.client)
        self.assertIsNotNone(order)
        self.assertEqual(len(order.items), 2)
        self.assertEqual(self.client._wishlist, [])
        self.assertAlmostEqual(order.get_total_price(), 18.5)

    def test_take_order_raises_empty_wishlist(self):
        self.client._wishlist = []
        with self.assertRaises(EmptyClientWishlistError):
            self.call_center.take_order(self.client)
