import unittest
from task1.MyList import MyList
from task1.MyClass import MyClass


class TestLibrarySort(unittest.TestCase):
    def test_sort_numbers(self):
        arr = [7, 16, 5, 0, 94, 2]
        my_list = MyList(arr)
        result = my_list.library_sort()
        self.assertEqual(result, [0, 2, 5, 7, 16, 94])

    def test_sort_strings(self):
        arr = ["ppois", "mois", "os", "bsuir", "os"]
        my_list = MyList(arr)
        result = my_list.library_sort()
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
        my_list = MyList(data)
        result = my_list.library_sort()
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
        my_list = MyList([])
        self.assertEqual(my_list.library_sort(), [])

    def test_one_element(self):
        my_list = MyList([MyClass(10)])
        self.assertEqual(my_list.library_sort(), [MyClass(10)])
