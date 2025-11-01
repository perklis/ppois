import unittest
from task1.MyClass import MyClass
from task1.spreadsort import spreadsort


class TestSpreadSort(unittest.TestCase):
    def test_sort_numbers(self):
        arr = [7, 16, 5, 0, 94, 2]
        result = spreadsort(arr)
        self.assertEqual(result, [0, 2, 5, 7, 16, 94])

    def test_sort_floats(self):
        arr = [3.2, 1.1, 4.5, 2.0, 2.5]
        result = spreadsort(arr)
        self.assertEqual(result, [1.1, 2.0, 2.5, 3.2, 4.5])

    def test_sort_strings(self):
        arr = ["ppois", "mois", "os", "bsuir", "os"]
        result = spreadsort(arr)
        self.assertEqual(result, ["bsuir", "mois", "os", "os", "ppois"])

    def test_sort_myclass(self):
        data = [
            MyClass(5),
            MyClass(7),
            MyClass(4),
            MyClass(12),
            MyClass(2),
            MyClass(9),
        ]

        result = spreadsort(data)

        expected = [
            MyClass(2),
            MyClass(4),
            MyClass(5),
            MyClass(7),
            MyClass(9),
            MyClass(12),
        ]

        self.assertEqual(result, expected)

    def test_empty_list(self):
        self.assertEqual(spreadsort([]), [])

    def test_one_element(self):
        self.assertEqual(spreadsort([MyClass(10)]), [MyClass(10)])
