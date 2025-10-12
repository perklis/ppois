import unittest
from employees.HeadPhysician import HeadPhysician
from employees.Doctor import Doctor
from employees.Economist import Economist
from employees.Lawyer import Lawyer
from security.SecurityDepartment import SecurityDepartment, SecurityReport


class TestHeadPhysician(unittest.TestCase):
    def setUp(self):
        self.head = HeadPhysician("Head Physician", "Dr. Smith", 50, 25, 5000)
        self.doctor1 = Doctor("Doctor", "Alice", 35, 10, 3000, "Cardiology", "Cardio")
        self.doctor2 = Doctor("Doctor", "Bob", 40, 15, 3500, "Neurology", "Neuro")
        self.head._HeadPhysician__doctors.extend([self.doctor1, self.doctor2])

        self.economist = Economist("Econ", 45, 20, "Finance", monthly_budget=20000)
        self.lawyer = Lawyer("Lawyer John", 38, 12, 4000)
        self.security_dept = SecurityDepartment("Main Security")

    def test_list_doctors(self):
        doctors_list = self.head.list_doctors()
        self.assertIn("Alice", doctors_list)
        self.assertIn("Bob", doctors_list)

    def test_get_doctor_schedule_no_schedule(self):
        schedule = self.head.get_doctor_schedule(self.doctor1)
        self.assertEqual(schedule, [])

    def test_get_doctor_schedule_wrong_doctor(self):
        other_doctor = Doctor("Doctor", "Eve", 30, 5, 2500, "Dermatology", "Skin")
        with self.assertRaises(PermissionError):
            self.head.get_doctor_schedule(other_doctor)

    def test_give_bonus_to_employees(self):
        self.economist.get_all_employees = lambda: [self.doctor1, self.doctor2]
        self.doctor1._set_salary(14000)
        self.doctor2._set_salary(16000)
        self.head.give_bonus_to_employees(
            self.economist, threshold=15000, bonus_percent=10
        )
        self.assertAlmostEqual(self.doctor1.get_salary(), 14000 * 1.1)
        self.assertEqual(self.doctor2.get_salary(), 16000)

    def test_request_security_report(self):
        report1 = SecurityReport("Guard1", "Incident 1")
        self.security_dept.collect_report(report1)
        result = self.head.request_security_report(self.security_dept)
        self.assertIn("Incident 1", result)

    def test_request_security_report_invalid_type(self):
        with self.assertRaises(TypeError):
            self.head.request_security_report("NotASecurityDept")

    def test_request_legal_report(self):
        self.lawyer.add_case("Case 1")
        self.lawyer.add_complaint("Complaint 1")
        report = self.head.request_legal_report(self.lawyer)
        self.assertIn("Case 1", report["cases"])
        self.assertIn("Complaint 1", report["complaints"])

    def test_request_legal_report_invalid_type(self):
        with self.assertRaises(TypeError):
            self.head.request_legal_report("NotALawyer")
