import unittest
from buffet.FoodItem import FoodItem
from buffet.FoodStock import FoodStock
from exceptions import NotEnoughItemError, ItemNotFound


class TestFoodStock(unittest.TestCase):
    def setUp(self):
        self.stock = FoodStock()
        self.apple = FoodItem("Apple", 5.0, 10)
        self.juice = FoodItem("Juice", 3.0, 2)
        self.stock.add_item(self.apple)
        self.stock.add_item(self.juice)

    def test_add_item_new(self):
        banana = FoodItem("Banana", 2.0, 5)
        self.stock.add_item(banana)
        self.assertIn("Banana", self.stock.items)
        self.assertEqual(self.stock.items["Banana"].quantity, 5)

    def test_add_item_existing(self):
        more_apples = FoodItem("Apple", 5.0, 5)
        self.stock.add_item(more_apples)
        self.assertEqual(self.stock.items["Apple"].quantity, 15)  # 10 + 5

    def test_sell_item_success(self):
        price = self.stock.sell_item(self.apple, 3)
        self.assertEqual(price, 15.0)
        self.assertEqual(self.stock.items["Apple"].quantity, 7)

    def test_sell_item_not_enough(self):
        with self.assertRaises(NotEnoughItemError):
            self.stock.sell_item(self.apple, 20)

    def test_sell_item_not_found(self):
        orange = FoodItem("Orange", 4.0, 5)
        with self.assertRaises(ItemNotFound):
            self.stock.sell_item(orange, 2)

    def test_check_stock_true(self):
        self.assertTrue(self.stock.check_stock(self.apple, 5))

    def test_check_stock_false(self):
        self.assertFalse(self.stock.check_stock(self.apple, 20))

    def test_show_low_stock(self):
        result = self.stock.show_low_stock()
        self.assertIn("Juice", result)
        self.assertNotIn("Apple", result)
