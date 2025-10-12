import unittest
from employees.Laborant import Laborant, LabTest
from patients.Patient import Patient
from patients.MedicalCard import MedicalCard


class TestLaborant(unittest.TestCase):
    def setUp(self):
        self.laborant = Laborant("Alice", 30, 5, salary=3000)
        self.patient = Patient("Bob", "123 Street", "555-1234", "Company", 1990)
        self.medical_card = MedicalCard(self.patient.name, self.patient.birth_year)
        self.patient.assign_medical_card(self.medical_card)
        self.test1 = LabTest("Blood Sugar", "0-120", "mg/dL")
        self.test2 = LabTest("Cholesterol", "0-200", "mg/dL")

    def test_initial_state(self):
        self.assertEqual(self.laborant.completed_tests, [])

    def test_perform_test_adds_result(self):
        result_message = self.laborant.perform_test(self.patient, self.test1)
        self.assertIn("Analysis for Bob (Blood Sugar) are done", result_message)
        self.assertEqual(len(self.laborant.completed_tests), 1)
        self.assertEqual(len(self.patient.get_medical_card().analyses), 1)

    def test_perform_multiple_tests(self):
        self.laborant.perform_test(self.patient, self.test1)
        self.laborant.perform_test(self.patient, self.test2)
        self.assertEqual(len(self.laborant.completed_tests), 2)
        self.assertEqual(len(self.patient.get_medical_card().analyses), 2)

    def test_list_completed_tests_empty(self):
        self.assertEqual(self.laborant.list_completed_tests(), "No tests performed yet")

    def test_list_completed_tests_non_empty(self):
        self.laborant.perform_test(self.patient, self.test1)
        output = self.laborant.list_completed_tests()
        self.assertIn("Blood Sugar", output)
        self.assertIn(str(self.laborant.completed_tests[0].value), output)
