import unittest
from employees.Hygienist import Hygienist
from employees.Orderly import Orderly


class TestHygienist(unittest.TestCase):
    def setUp(self):
        self.hygienist = Hygienist("Anna", 35, 10, salary=2500)
        self.orderly1 = Orderly("John", 28, 3, salary=1200)
        self.orderly2 = Orderly("Mike", 30, 5, salary=1300)

    def test_initial_state(self):
        self.assertEqual(self.hygienist.list_trained_orderlies(), [])
        self.assertEqual(self.hygienist._trainings_conducted, 0)

    def test_conduct_training_updates_orderlies(self):
        self.hygienist.conduct_training("Hand Hygiene", [self.orderly1, self.orderly2])
        self.assertIn("John", self.hygienist.list_trained_orderlies())
        self.assertIn("Mike", self.hygienist.list_trained_orderlies())
        self.assertEqual(self.hygienist._trainings_conducted, 1)

    def test_multiple_trainings(self):
        self.hygienist.conduct_training("Hand Hygiene", [self.orderly1])
        self.hygienist.conduct_training("Equipment Cleaning", [self.orderly2])
        self.assertEqual(len(self.hygienist.list_trained_orderlies()), 2)

    def test_orderly_training_info(self):
        self.hygienist.conduct_training("Hand Hygiene", [self.orderly1])
        self.assertIn("Hand Hygiene", self.orderly1._trained_topics)
        self.assertEqual(self.orderly1._last_instructor, "Anna")
