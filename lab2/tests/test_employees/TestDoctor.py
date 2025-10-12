import unittest
from employees.Doctor import Doctor
from patients.Patient import Patient
from patients.MedicalCard import MedicalCard
from schedule.DoctorSchedule import DoctorSchedule
from exceptions import DoctorScheduleError


class TestDoctor(unittest.TestCase):
    def setUp(self):
        self.doctor = Doctor(
            job_title="Therapist",
            name="John Doe",
            age=40,
            work_experience=15,
            salary=2500,
            specialisation="Therapy",
            department="Internal Medicine",
        )

        self.patient = Patient(
            name="Alice Smith",
            address="Main St 5",
            phone_number="123456789",
            workplace="Office",
            birth_year=1990,
        )
        self.card = MedicalCard(self.patient.name, self.patient.birth_year)
        self.patient.assign_medical_card(self.card)

        self.schedule = DoctorSchedule(self.doctor)
        self.schedule.generate_week_talons("2025-10-13")
        self.doctor.set_schedule(self.schedule)

    def test_add_patient(self):
        self.doctor.add_patient(self.patient)
        self.assertIn(self.patient, self.doctor._patients)

    def test_add_diagnosis_success(self):
        self.doctor.add_patient(self.patient)
        self.doctor.add_diagnosis(self.patient, "2025-10-13", "Flu", ["Paracetamol"])
        visits = self.patient.medical_card.get_visits()
        self.assertEqual(len(visits), 1)
        self.assertEqual(visits[0]["diagnosis"], "Flu")

    def test_add_diagnosis_unregistered_patient(self):
        with self.assertRaises(DoctorScheduleError):
            self.doctor.add_diagnosis(self.patient, "2025-10-13", "Cold")

    def test_set_schedule_wrong_doctor(self):
        other_doc = Doctor(
            job_title="Cardiologist",
            name="Jane Roe",
            age=35,
            work_experience=10,
            salary=2200,
            specialisation="Cardiology",
            department="Heart Center",
        )
        wrong_schedule = DoctorSchedule(other_doc)
        with self.assertRaises(DoctorScheduleError):
            self.doctor.set_schedule(wrong_schedule)

    def test_see_patient_success(self):
        free_talon = self.schedule.get_free_talons()[0]
        talon = self.doctor.see_patient(
            patient=self.patient,
            date=free_talon.date,
            time_str=free_talon.time.strftime("%H:%M"),
            diagnosis="Cough",
            prescriptions=["Syrup"],
        )
        self.assertTrue(talon.is_taken)
        self.assertEqual(talon.patient, self.patient)
        self.assertEqual(
            self.patient.medical_card.get_visits()[-1]["diagnosis"], "Cough"
        )

    def test_see_patient_no_schedule(self):
        new_doc = Doctor(
            job_title="Therapist",
            name="NoScheduleDoc",
            age=30,
            work_experience=5,
            salary=1500,
            specialisation="Therapy",
            department="Internal",
        )
        with self.assertRaises(DoctorScheduleError):
            new_doc.see_patient(self.patient, "2025-10-13", "10:00", "Cold")
