import unittest
from employees.Clerk import Clerk
from employees.ProcurementSpecialist import ProcurementSpecialist


class TestClerk(unittest.TestCase):
    def setUp(self):
        self.clerk = Clerk(
            name="Maria",
            age=28,
            work_experience=4,
            salary=2000,
            department="Procurement",
        )
        self.specialist = ProcurementSpecialist(
            name="Ivan",
            age=35,
            work_experience=10,
            salary=4000,
            department="Procurement",
        )

    def test_initialization(self):
        self.assertEqual(self.clerk.name, "Maria")
        self.assertEqual(self.clerk.department, "Procurement")
        self.assertEqual(self.clerk.tasks, [])
        self.assertEqual(self.clerk.handled_documents, 0)

    def test_assign_task(self):
        self.clerk.assign_task("Check supplier invoices")
        self.assertIn("Check supplier invoices", self.clerk.tasks)

    def test_complete_existing_task(self):
        self.clerk.assign_task("Prepare report")
        self.clerk.complete_task("Prepare report")
        self.assertNotIn("Prepare report", self.clerk.tasks)
        self.assertEqual(self.clerk.handled_documents, 1)

    def test_complete_nonexistent_task(self):
        self.clerk.complete_task("Archive documents")
        self.assertEqual(self.clerk.handled_documents, 0)  # ничего не добавилось

    def test_receive_report(self):
        report_before = self.specialist.generate_report()
        self.assertIn("not made any purchases", report_before)
        self.clerk.receive_report(self.specialist)

        self.specialist.purchases.append({"item": "Paracetamol", "quantity": 40})
        report_after = self.specialist.generate_report()
        self.assertIn("Paracetamol", report_after)
