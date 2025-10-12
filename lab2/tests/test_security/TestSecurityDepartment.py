import unittest
from employees.SecurityGuard import SecurityGuard
from security.SecurityDepartment import SecurityDepartment
from security.SecurityReport import SecurityReport
from exceptions import GuardAlreadyExistsError, GuardNotFound, InvalidGuardTypeError


class TestSecurityDepartment(unittest.TestCase):
    def setUp(self):
        self.department = SecurityDepartment("Main Security")
        self.guard1 = SecurityGuard("John", 35, 10, 5000, "Night")
        self.guard2 = SecurityGuard("Alice", 30, 5, 4500, "Day")

    def test_add_guard_success(self):
        msg = self.department.add_guard(self.guard1)
        self.assertIn("added", msg)
        self.assertIn(self.guard1, self.department.get_on_duty_guards() + [self.guard1])

    def test_add_guard_duplicate(self):
        self.department.add_guard(self.guard1)
        with self.assertRaises(GuardAlreadyExistsError):
            self.department.add_guard(self.guard1)

    def test_add_guard_wrong_type(self):
        with self.assertRaises(InvalidGuardTypeError):
            self.department.add_guard("not a guard")

    def test_remove_guard_success(self):
        self.department.add_guard(self.guard1)
        msg = self.department.remove_guard(self.guard1)
        self.assertIn("removed", msg)

    def test_remove_guard_not_found(self):
        with self.assertRaises(GuardNotFound):
            self.department.remove_guard(self.guard2)

    def test_get_on_duty_guards(self):
        self.guard1.start_shift()
        self.guard2.start_shift()
        self.department.add_guard(self.guard1)
        self.department.add_guard(self.guard2)
        on_duty = self.department.get_on_duty_guards()
        self.assertIn(self.guard1, on_duty)
        self.assertIn(self.guard2, on_duty)

    def test_collect_and_show_reports(self):
        report1 = SecurityReport("John", "Incident A")
        report2 = SecurityReport("Alice", "Incident B")
        self.department.collect_report(report1)
        self.department.collect_report(report2)
        output = self.department.show_all_reports()
        self.assertIn("Incident A", output)
        self.assertIn("Incident B", output)

    def test_assign_shift_success(self):
        self.department.add_guard(self.guard1)
        msg = self.department.assign_shift(self.guard1, "Morning")
        self.assertIn("assigned", msg)
        self.assertEqual(self.guard1.shift_type, "Morning")

    def test_assign_shift_guard_not_in_department(self):
        with self.assertRaises(GuardNotFound):
            self.department.assign_shift(self.guard1, "Morning")

    def test_str_representation(self):
        self.department.add_guard(self.guard1)
        self.guard1.start_shift()
        s = str(self.department)
        self.assertIn("Total guards", s)
        self.assertIn("On duty", s)
        self.assertIn(self.department.department_name, s)
