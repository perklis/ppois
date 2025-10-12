import unittest
from employees.Pharmacist import Pharmacist
from pharmacy.Pharmacy import Pharmacy
from pharmacy.Medication import Medication
from exceptions import NoPharmacistAssignedError, NotEnoughItemError


class TestPharmacy(unittest.TestCase):
    def setUp(self):
        self.pharmacy = Pharmacy("HealthPlus")
        self.pharmacist = Pharmacist("Anna", 30, 5, 4000)
        self.med1 = Medication("Paracetamol", 50, "pcs")
        self.med2 = Medication("Ibuprofen", 30, "pcs")

    def test_hire_pharmacist_and_list(self):
        self.pharmacy.hire_pharmacist(self.pharmacist)
        pharmacists_list = self.pharmacy.list_pharmacists()
        self.assertIn("Anna", pharmacists_list)

    def test_add_medication_to_inventory(self):
        self.pharmacy.hire_pharmacist(self.pharmacist)
        msg = self.pharmacy.add_medication_to_inventory(self.med1)
        self.assertIn("50 pcs of Paracetamol added", msg)

    def test_add_medication_no_pharmacist_raises(self):
        with self.assertRaises(NoPharmacistAssignedError):
            self.pharmacy.add_medication_to_inventory(self.med1)

    def test_dispense_medication_success(self):
        self.pharmacy.hire_pharmacist(self.pharmacist)
        self.pharmacy.add_medication_to_inventory(self.med1)
        msg = self.pharmacy.dispense_to_patient("Paracetamol", 20)
        self.assertIn("20 pcs of Paracetamol dispensed", msg)

    def test_dispense_medication_not_enough_raises(self):
        self.pharmacy.hire_pharmacist(self.pharmacist)
        self.pharmacy.add_medication_to_inventory(self.med2)
        with self.assertRaises(NotEnoughItemError):
            self.pharmacy.dispense_to_patient("Ibuprofen", 50)

    def test_dispense_medication_no_pharmacist_raises(self):
        with self.assertRaises(NoPharmacistAssignedError):
            self.pharmacy.dispense_to_patient("Paracetamol", 10)

    def test_check_medication_stock(self):
        self.pharmacy.hire_pharmacist(self.pharmacist)
        self.pharmacy.add_medication_to_inventory(self.med1)
        stock_msg = self.pharmacy.check_medication_stock("Paracetamol")
        self.assertIn("50 pcs in stock", stock_msg)

    def test_check_medication_stock_no_pharmacist_raises(self):
        with self.assertRaises(NoPharmacistAssignedError):
            self.pharmacy.check_medication_stock("Paracetamol")
