import unittest
from employees.SecurityGuard import SecurityGuard
from employees.Engineer import Engineer
from equipment.Equipment import Equipment


class TestSecurityGuard(unittest.TestCase):
    def setUp(self):
        self.guard = SecurityGuard("John", 35, 10, 5000, "Night")
        self.engineer = Engineer("Alice", 30, 5, "Mechanical", "Maintenance", 7000)
        self.equipment_working = Equipment("Ventilator", "V123")
        self.equipment_broken = Equipment("ECG", "E456")

    def test_start_and_end_shift(self):
        msg_start = self.guard.start_shift()
        self.assertTrue(self.guard.is_on_duty())
        self.assertIn("started", msg_start)

        msg_end = self.guard.end_shift()
        self.assertFalse(self.guard.is_on_duty())
        self.assertIn("ended", msg_end)

    def test_report_incident_returns_report(self):
        report = self.guard.report_incident("Test incident")
        self.assertEqual(report.guard_name, "John")
        self.assertEqual(report.description, "Test incident")

    def test_notify_engineer_with_working_equipment(self):
        msg = self.guard.notify_engineer(self.engineer, self.equipment_working)
        self.assertEqual(self.equipment_working.condition, "Working")
        self.assertIn("working fine", msg)

    def test_notify_engineer_with_broken_equipment(self):
        self.equipment_broken.break_down()
        self.engineer.add_equipment(self.equipment_broken)
        msg = self.guard.notify_engineer(self.engineer, self.equipment_broken)
        self.assertEqual(self.equipment_broken.condition, "Working")
        self.assertIn("reported", msg)
        self.assertIn("repaired", msg)

    def test_str_representation(self):
        self.guard.start_shift()
        s = str(self.guard)
        self.assertIn("on duty", s)
        self.assertIn("John", s)
