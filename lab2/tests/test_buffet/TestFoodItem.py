import unittest
from buffet.FoodItem import FoodItem
from exceptions import NotEnoughItemError


class TestFoodItem(unittest.TestCase):
    def setUp(self):
        self.apple = FoodItem("Apple", 5.0, 10)

    def test_reduce_quantity_success(self):
        self.apple.reduce_quantity(3)
        self.assertEqual(self.apple.quantity, 7)

    def test_reduce_quantity_not_enough(self):
        with self.assertRaises(NotEnoughItemError):
            self.apple.reduce_quantity(20)

    def test_add_quantity(self):
        self.apple.add_quantity(5)
        self.assertEqual(self.apple.quantity, 15)

    def test_repr(self):
        self.assertEqual(repr(self.apple), "Apple - 10 pcs for 5.0₽")
