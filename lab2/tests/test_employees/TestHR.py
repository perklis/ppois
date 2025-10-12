import unittest
from employees.HR import HR
from employees.Employee import Employee
from employees.Doctor import Doctor
from employees.HeadPhysician import HeadPhysician


class TestHR(unittest.TestCase):
    def setUp(self):
        self.hr = HR("Alice", 30, 5, 2500, total_employees=10)
        self.employee = Employee("Engineer", "Bob", 28, 3, 2000)
        self.doctor = Doctor("Doctor", "Gregory", 45, 20, 4000, "Cardiology", "Heart")
        self.head_physician = HeadPhysician("Head Physician", "Dr. House", 50, 25, 6000)

    def test_count_all_employees_property(self):
        self.assertEqual(self.hr.count_all_employees, 10)

    def test_hire_employee_success(self):
        msg = self.hr.hire_employee(self.employee)
        self.assertEqual(self.hr.count_all_employees, 11)
        self.assertIn("hired Engineer Bob", msg)

    def test_hire_employee_doctor_permission_error(self):
        with self.assertRaises(PermissionError):
            self.hr.hire_employee(self.doctor)

    def test_hire_employee_head_physician_permission_error(self):
        with self.assertRaises(PermissionError):
            self.hr.hire_employee(self.head_physician)

    def test_fire_employee_success(self):
        msg = self.hr.fire_employee(self.employee)
        self.assertEqual(self.hr.count_all_employees, 9)
        self.assertIn("fired Engineer Bob", msg)

    def test_fire_employee_doctor_permission_error(self):
        with self.assertRaises(PermissionError):
            self.hr.fire_employee(self.doctor)

    def test_fire_employee_head_physician_permission_error(self):
        with self.assertRaises(PermissionError):
            self.hr.fire_employee(self.head_physician)

    def test_fire_employee_count_not_negative(self):
        hr = HR("Eve", 29, 4, 2300, total_employees=0)
        hr.fire_employee(self.employee)
        self.assertEqual(hr.count_all_employees, 0)

    def test_make_interview_too_young(self):
        result = self.hr.make_interview("Jake", 19, 3)
        self.assertIn("too young", result)

    def test_make_interview_insufficient_experience(self):
        result = self.hr.make_interview("Tom", 25, 1)
        self.assertIn("insufficient experience", result)

    def test_make_interview_successful(self):
        result = self.hr.make_interview("Mia", 26, 3)
        self.assertIn("passed the interview", result)

    def test_str_representation(self):
        result = str(self.hr)
        self.assertIn("HR Alice", result)
        self.assertIn("experience: 5 years", result)
