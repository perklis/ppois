import unittest
from unittest.mock import Mock, patch
from client.Client import Client
from exceptions import EmptyClientWishlistError, AdressNotInDeliveryZone


class TestClient(unittest.TestCase):
    def setUp(self):
        self.addr = Mock()
        self.addr.street = "Lenina"
        self.addr.city = "Grodno"
        self.client = Client("Olya", "89001112233", self.addr)

    def test_add_and_remove_wishlist(self):
        item = Mock()
        item.name = "Pizza"
        item.price = 15

        self.client.add_to_wishlist(item)
        self.assertIn(item, self.client._wishlist)

        self.client.remove_from_wishlist("Pizza")
        self.assertNotIn(item, self.client._wishlist)

    def test_make_order_ok(self):
        item = Mock()
        item.name = "Burger"
        item.price = 8.0
        self.client._wishlist.append(item)

        with (
            patch("client.Client.DeliveryZone") as mock_zone_cls,
            patch("client.Client.Order") as mock_order_cls,
        ):
            zone = mock_zone_cls.return_value
            zone.is_in_zone.return_value = True

            order = mock_order_cls.return_value
            order.add_item = Mock()
            order.pay = Mock()

            result = self.client.make_order()

            order.add_item.assert_called_once()
            order.pay.assert_called_once()
            self.assertEqual(result, order)
            self.assertEqual(len(self.client._wishlist), 0)

    def test_make_order_empty(self):
        with self.assertRaises(EmptyClientWishlistError):
            self.client.make_order()

    def test_make_order_not_in_zone(self):
        item = Mock()
        item.name = "Pasta"
        item.price = 10.0
        self.client._wishlist.append(item)

        with patch("client.Client.DeliveryZone") as mock_zone_cls:
            zone = mock_zone_cls.return_value
            zone.is_in_zone.return_value = False

            with self.assertRaises(AdressNotInDeliveryZone):
                self.client.make_order()

    def test_check_weather(self):
        weather = Mock()
        weather.get_weather.return_value = "sunny"
        self.client._Client__weather = weather

        result = self.client.check_weather()
        weather.get_weather.assert_called_once_with(self.addr.city)
        self.assertEqual(result, "sunny")
