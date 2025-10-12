import unittest
from employees.Doctor import Doctor
from patients.Patient import Patient
from patients.MedicalCard import MedicalCard
from ambulance.EmergencyRoom import EmergencyRoom
from exceptions import NoMedicalCardError


class TestEmergencyRoom(unittest.TestCase):
    def setUp(self):
        self.doctor = Doctor(
            job_title="Dr.",
            name="John",
            age=40,
            work_experience=15,
            salary=5000,
            specialisation="Cardiology",
            department="Emergency",
        )
        self.er = EmergencyRoom(101, self.doctor)
        self.patient_with_card = Patient("Alice", "Lenina 10", "123456", "BSUIR", 1990)
        self.patient_with_card.assign_medical_card(
            MedicalCard(
                patient_name=self.patient_with_card.name,
                birth_year=self.patient_with_card.birth_year,
            )
        )
        self.patient_without_card = Patient("Bob", "Lenina 11", "654321", "BSUIR", 1985)

    def test_admit_patient(self):
        self.er.admit_patient(self.patient_with_card, "headache")
        self.assertEqual(self.er.current_patient, self.patient_with_card)

    def test_diagnose_and_treat_success(self):
        self.er.admit_patient(self.patient_with_card, "fever")
        self.er.diagnose_and_treat("Flu", "moderate")
        self.assertIsNone(self.er.current_patient)
        self.assertEqual(
            self.patient_with_card.get_medical_card().sicknesses[-1].name, "Flu"
        )
        self.assertIn(self.patient_with_card, self.doctor._patients)

    def test_diagnose_and_treat_no_patient(self):
        self.er.diagnose_and_treat("Flu", "moderate")
        self.assertIsNone(self.er.current_patient)

    def test_diagnose_and_treat_no_medical_card(self):
        self.er.admit_patient(self.patient_without_card, "injury")
        with self.assertRaises(NoMedicalCardError):
            self.er.diagnose_and_treat("Fracture", "severe")
