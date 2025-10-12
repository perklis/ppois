import unittest
from ambulance.Ambulance import Ambulance
from ambulance.Paramedic import Paramedic
from ambulance.EmergencyCall import EmergencyCall
from patients.Patient import Patient


class TestAmbulance(unittest.TestCase):
    def setUp(self):
        self.ambulance = Ambulance("A123", "Ivan")
        self.paramedic = Paramedic("Paramedic", "Kate", 30, 5, 1000)
        self.patient = Patient("Alex", "Lenina 10", "123456", "BSUIR", 1990)
        self.call = EmergencyCall(self.patient, "Lenina 10", "Heart pain")

    def test_assign_paramedic(self):
        self.ambulance.assign_paramedic(self.paramedic)
        self.assertEqual(self.ambulance.paramedic, self.paramedic)
        self.assertEqual(self.paramedic.ambulance, self.ambulance)

    def test_receive_call(self):
        self.ambulance.receive_call(self.call)
        self.assertEqual(self.ambulance.current_call, self.call)

    def test_complete_call_with_active_call(self):
        self.ambulance.receive_call(self.call)
        self.ambulance.complete_call()
        self.assertIsNone(self.ambulance.current_call)

    def test_complete_call_no_active_call(self):
        self.ambulance.complete_call()
        self.assertIsNone(self.ambulance.current_call)
