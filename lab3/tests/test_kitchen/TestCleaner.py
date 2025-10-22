import unittest
from restaurant.kitchen.Cleaner import Cleaner
from exceptions import CleaningError


class TestCleaner(unittest.TestCase):
    def setUp(self):
        self.cleaner = Cleaner("Bob", 1500.0, "123456789")

    def test_clean_room_increments_count(self):
        self.cleaner.clean_room("Kitchen")
        self.assertEqual(self.cleaner.cleaned_rooms, 1)

    def test_tools_not_ready(self):
        self.cleaner.tools_ready = False
        with self.assertRaises(CleaningError):
            self.cleaner.clean_room("Bathroom")

    def test_prepare_tools_sets_tools_ready(self):
        self.cleaner.tools_ready = False
        self.cleaner.prepare_tools()
        self.assertTrue(self.cleaner.tools_ready)

    def test_report_prints(self):
        self.cleaner.clean_room("Sick")
        self.cleaner.report()

    def test_take_break_prints(self):
        self.cleaner.take_break()
