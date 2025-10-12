import unittest
from buffet.BuffetWorker import BuffetWorker
from buffet.FoodItem import FoodItem
from buffet.FoodStock import FoodStock
from patients.Patient import Patient
from exceptions import NotEnoughItemError


class TestBuffetWorker(unittest.TestCase):
    def setUp(self):
        self.worker = BuffetWorker("Kate", 25, 2, 780)
        self.stock = FoodStock()
        self.apple = FoodItem("Apple", 5.0, 10)
        self.stock.add_item(self.apple)
        self.patient = Patient("Alexander", "Lenina 10", "123456", "BSUIR", 1985)

    def test_sell_food_success(self):
        price = self.worker.sell_food(self.stock, self.patient, self.apple, 3)
        self.assertEqual(price, 15.0)
        self.assertEqual(self.worker.sales_total, 15.0)
        self.assertEqual(self.stock.items["Apple"].quantity, 7)

    def test_sell_food_not_enough(self):
        with self.assertRaises(NotEnoughItemError):
            self.worker.sell_food(self.stock, self.patient, self.apple, 20)

    def test_sales_total_accumulates(self):
        self.worker.sell_food(self.stock, self.patient, self.apple, 2)
        self.worker.sell_food(self.stock, self.patient, self.apple, 3)
        self.assertEqual(self.worker.sales_total, 25.0)  # 2*5 + 3*5
