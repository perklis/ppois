import unittest
from employees.Pharmacist import Pharmacist
from pharmacy.Medication import Medication


class TestPharmacist(unittest.TestCase):
    def setUp(self):
        self.pharmacist = Pharmacist("Anna", 30, 5, 4000)
        self.med1 = Medication("Paracetamol", 50, "pcs")
        self.med2 = Medication("Ibuprofen", 30, "pcs")

    def test_add_medication_updates_inventory(self):
        msg = self.pharmacist.add_medication(self.med1)
        self.assertIn("50 pcs of Paracetamol added", msg)
        self.assertEqual(self.pharmacist._inventory.get_quantity("Paracetamol"), 50)

    def test_check_stock_returns_correct_quantity(self):
        self.pharmacist.add_medication(self.med2)
        stock_msg = self.pharmacist.check_stock("Ibuprofen")
        self.assertIn("30 pcs in stock", stock_msg)

    def test_dispense_medication_reduces_inventory(self):
        self.pharmacist.add_medication(self.med1)
        msg = self.pharmacist.dispense_medication("Paracetamol", 20)
        self.assertIn("20 pcs of Paracetamol dispensed", msg)
        self.assertEqual(self.pharmacist._inventory.get_quantity("Paracetamol"), 30)

    def test_dispense_medication_not_enough(self):
        self.pharmacist.add_medication(self.med2)
        msg = self.pharmacist.dispense_medication("Ibuprofen", 50)
        self.assertIn("Not enough Ibuprofen", msg)

    def test_generate_inventory_report(self):
        self.pharmacist.add_medication(self.med1)
        self.pharmacist.add_medication(self.med2)
        report = self.pharmacist.generate_inventory_report()
        self.assertIn("Paracetamol: 50 pcs", report)
        self.assertIn("Ibuprofen: 30 pcs", report)

    def test_generate_inventory_report_empty(self):
        empty_report = self.pharmacist.generate_inventory_report()
        self.assertEqual(empty_report, "Inventory is empty")
