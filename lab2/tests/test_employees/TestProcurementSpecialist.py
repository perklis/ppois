import unittest
from employees.ProcurementSpecialist import ProcurementSpecialist
from employees.Pharmacist import Pharmacist
from pharmacy.Pharmacy import Pharmacy


class TestProcurementSpecialist(unittest.TestCase):
    def setUp(self):
        self.specialist = ProcurementSpecialist(
            name="Dmitry",
            age=40,
            work_experience=15,
            salary=5000,
            department="Procurement",
        )
        self.pharmacy = Pharmacy("Central Pharmacy")
        self.pharmacist = Pharmacist("Olga", 30, 5, 3000)
        self.pharmacy.hire_pharmacist(self.pharmacist)

    def test_initialization(self):
        self.assertEqual(self.specialist.name, "Dmitry")
        self.assertEqual(self.specialist.department, "Procurement")
        self.assertEqual(self.specialist.purchases, [])

    def test_order_medication_adds_to_purchases(self):
        inventory = self.pharmacist._inventory
        self.specialist._order_medication(inventory, "Aspirin", 30)
        self.assertTrue(any(p["item"] == "Aspirin" for p in self.specialist.purchases))
        self.assertGreater(inventory.get_quantity("Aspirin"), 0)

    def test_generate_report_empty(self):
        report = self.specialist.generate_report()
        self.assertIn("not made any purchases", report)

    def test_generate_report_with_purchases(self):
        inventory = self.pharmacist._inventory
        self.specialist._order_medication(inventory, "Ibuprofen", 50)
        report = self.specialist.generate_report()
        self.assertIn("Ibuprofen", report)
        self.assertIn("50", report)

    def test_monthly_procurement_adds_common_meds(self):
        self.specialist.monthly_procurement(self.pharmacy)
        meds_in_inventory = list(self.pharmacist._inventory._medications.keys())
        self.assertIn("Paracetamol", meds_in_inventory)
        self.assertIn("Ibuprofen", meds_in_inventory)
        self.assertIn("Acyclovir", meds_in_inventory)
        self.assertGreater(len(self.specialist.purchases), 0)
