import unittest
from delivery.DeliveryEmployee import DeliveryEmployee


class TestDeliveryEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = DeliveryEmployee(
            name="Gendos",
            phone="1234567890",
            salary=1000.0,
            experience=2,
            department="Delivery",
        )

    def test_initial_state(self):
        self.assertEqual(self.emp.name, "Gendos")
        self.assertEqual(self.emp.phone, "1234567890")
        self.assertEqual(self.emp.salary, 1000.0)
        self.assertEqual(self.emp.experience, 2)
        self.assertEqual(self.emp.department, "Delivery")
        self.assertFalse(self.emp.on_shift)
        self.assertEqual(self.emp.tasks_done, 0)

    def test_start_shift(self):
        self.emp.start_shift()
        self.assertTrue(self.emp.on_shift)

    def test_end_shift(self):
        self.emp.start_shift()
        self.emp.end_shift()
        self.assertFalse(self.emp.on_shift)

    def test_complete_task(self):
        self.emp.complete_task()
        self.assertEqual(self.emp.tasks_done, 1)
        self.emp.complete_task()
        self.assertEqual(self.emp.tasks_done, 2)

    def test_get_info(self):
        info = self.emp.get_info()
        self.assertIn("Gendos", info)
        self.assertIn("Delivery", info)
        self.assertIn("Experience: 2 years", info)
        self.assertIn("On shift: False", info)
        self.assertIn("Tasks done: 0", info)

    def test_str(self):
        s = str(self.emp)
        self.assertEqual(s, "Gendos: (Delivery), 2 yrs exp")
