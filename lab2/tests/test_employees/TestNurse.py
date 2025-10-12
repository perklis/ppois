import unittest
from employees.Nurse import Nurse
from patients.Patient import Patient
from patients.MedicalCard import MedicalCard
from patients.Sickness import Sickness
from schedule.Talon import Talon
from laboratory.Laboratory import Laboratory


class TestNurse(unittest.TestCase):
    def setUp(self):
        self.nurse = Nurse("Nurse", "Anna", 32, 7, 3000, "Cardiology")
        self.patient = Patient("Bob", "123 Street", "555-1234", "Company", 1985)
        self.patient.assign_medical_card(
            MedicalCard(self.patient.name, self.patient.birth_year)
        )
        self.sickness = Sickness("Flu", ["fever", "cough"], "Mild")
        self.talon = Talon("2025-10-12", "09:00", doctor=None)
        self.lab = Laboratory()

    def test_initial_state(self):
        self.assertEqual(self.nurse._patient_records, {})

    def test_admit_patient_creates_report(self):
        msg = self.nurse.admit_patient(
            self.patient, self.sickness, self.talon, 80, "120/80", 175, 70
        )
        self.assertIn("Nurse Anna admitted patient Bob", msg)
        self.assertIn(self.patient, self.nurse._patient_records)
        self.assertEqual(len(self.nurse._patient_records[self.patient]), 1)
        self.assertEqual(len(self.patient.get_medical_card().visits), 1)

    def test_view_patient_reports_returns_reports(self):
        self.nurse.admit_patient(
            self.patient, self.sickness, self.talon, 80, "120/80", 175, 70
        )
        reports_text = self.nurse.view_patient_reports(self.patient)
        self.assertIn("Reports for Bob", reports_text)
        self.assertIn("Flu", reports_text)

    def test_view_patient_reports_no_reports(self):
        new_patient = Patient("Alice", "456 Street", "555-5678", "Company", 1990)
        reports_text = self.nurse.view_patient_reports(new_patient)
        self.assertIn("No reports found for Alice", reports_text)

    def test_write_referral_for_admitted_patient(self):
        self.nurse.admit_patient(
            self.patient, self.sickness, self.talon, 80, "120/80", 175, 70
        )
        msg = self.nurse.write_referral(self.lab, self.patient, "Blood Test")
        self.assertIn("Nurse Anna issued referral for Bob", msg)
        self.assertTrue(self.lab.check_referral(self.patient.name, "Blood Test"))

    def test_write_referral_for_unadmitted_patient(self):
        new_patient = Patient("Charlie", "789 Street", "555-9876", "Company", 1992)
        msg = self.nurse.write_referral(self.lab, new_patient, "Blood Test")
        self.assertIn("cannot issue referral", msg)
        self.assertFalse(self.lab.check_referral(new_patient.name, "Blood Test"))
