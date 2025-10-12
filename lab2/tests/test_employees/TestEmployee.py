import unittest
from employees.Employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee(
            job_title="Nurse",
            name="Alice",
            age=28,
            work_experience=3,
            salary=1500.0,
        )

    def test_initialization(self):
        self.assertEqual(self.employee.job_title, "Nurse")
        self.assertEqual(self.employee.name, "Alice")
        self.assertEqual(self.employee.age, 28)
        self.assertEqual(self.employee.work_experience, 3)
        self.assertEqual(self.employee.get_salary(), 0.0)

    def test_get_information(self):
        info = self.employee.get_information()
        self.assertIn("Nurse", info)
        self.assertIn("Alice", info)
        self.assertIn("Work length: 3 years", info)

    def test_add_experience_default(self):
        result = self.employee.add_experience()
        self.assertEqual(self.employee.work_experience, 4)
        self.assertIn("Work expirience Alice increases", result)

    def test_add_experience_custom_years(self):
        result = self.employee.add_experience(5)
        self.assertEqual(self.employee.work_experience, 8)
        self.assertIn("8 years", result)

    def test_set_and_get_salary(self):
        self.employee._set_salary(2500.0)
        self.assertEqual(self.employee.get_salary(), 2500.0)
