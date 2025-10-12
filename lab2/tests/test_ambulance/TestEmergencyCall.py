import unittest
from ambulance.EmergencyCall import EmergencyCall
from patients.Patient import Patient


class TestEmergencyCall(unittest.TestCase):
    def setUp(self):
        self.patient = Patient("Alex", "Lenina 10", "123456", "BSUIR", 1990)
        self.call = EmergencyCall(self.patient, "Lenina 10", "Heart pain")

    def test_initial_status(self):
        self.assertEqual(self.call.status, "pending")
        self.assertEqual(self.call.patient, self.patient)
        self.assertEqual(self.call.address, "Lenina 10")
        self.assertEqual(self.call.reason, "Heart pain")

    def test_accept_call(self):
        self.call.accept()
        self.assertEqual(self.call.status, "accepted")

    def test_complete_call(self):
        self.call.complete()
        self.assertEqual(self.call.status, "completed")
