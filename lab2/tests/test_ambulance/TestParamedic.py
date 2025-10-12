import unittest
from ambulance.Paramedic import Paramedic
from patients.Patient import Patient
from patients.MedicalCard import MedicalCard


class TestParamedic(unittest.TestCase):
    def setUp(self):
        self.paramedic = Paramedic("Paramedic", "Alex", 30, 5, 2500)
        self.patient = Patient("Ivan", "Main St 10", "123456", "Plant", 1995)

    def test_init(self):
        self.assertEqual(self.paramedic.name, "Alex")
        self.assertIsNone(self.paramedic.ambulance)

    def test_provide_first_aid_with_medical_card(self):
        card = MedicalCard(
            patient_name=self.patient.name, birth_year=self.patient.birth_year
        )
        self.patient.assign_medical_card(card)

        self.paramedic.provide_first_aid(self.patient, "head injury")

        visits = self.patient.get_medical_card().visits
        found = any("First aid for head injury" in str(v) for v in visits)
        self.assertTrue(found)

    def test_provide_first_aid_without_medical_card(self):
        self.paramedic.provide_first_aid(self.patient, "bruise")

    def test_transport_patient(self):
        self.paramedic.transport_patient(self.patient, "City Hospital")
