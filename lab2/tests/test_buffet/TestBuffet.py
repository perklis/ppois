import unittest
from buffet.Buffet import Buffet
from buffet.FoodItem import FoodItem
from buffet.FoodStock import FoodStock
from buffet.BuffetWorker import BuffetWorker
from patients.Patient import Patient


class TestBuffet(unittest.TestCase):
    def setUp(self):
        self.stock = FoodStock()
        self.item = FoodItem("Apple", 5.0, 30)
        self.stock.add_item(self.item)
        self.worker = BuffetWorker("Kate", 25, 2, 780)
        self.buffet = Buffet(self.stock, self.worker)
        self.patient = Patient("Alexander", "Lenina 10", "123456", "BSUIR", 1985)

    def test_sell_to_patient(self):
        result = self.buffet.sell_to_patient(self.patient, self.item, 3)
        self.assertEqual(result, 15.0)

    def test_check_stock(self):
        self.assertTrue(self.buffet.check_stock(self.item, 2))

    def test_show_low_stock(self):
        self.buffet.sell_to_patient(self.patient, self.item, 28)
        result = self.buffet.show_low_stock()
        self.assertIn("Apple", result)
