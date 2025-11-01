import unittest
from task2.iters.ConstTwoDirIterator import ConstTwoDirIterator
from task2.iters.ConstContainer import ConstContainer


class TestConstTwoDirIterator(unittest.TestCase):
    def setUp(self):
        self.items_int = [10, 20, 30]
        self.items_str = ["A", "B", "C"]

    def test_forward_iteration(self):
        it = ConstTwoDirIterator(self.items_int)

        a = next(it)
        self.assertIsInstance(a, ConstContainer)
        self.assertEqual(repr(a), "ConstContainer(10)")

        b = next(it)
        self.assertEqual(repr(b), "ConstContainer(20)")

        c = next(it)
        self.assertEqual(repr(c), "ConstContainer(30)")

        with self.assertRaises(StopIteration):
            next(it)

    def test_backward_iteration(self):
        it = ConstTwoDirIterator(self.items_int, start=3)

        a = it.prev()
        self.assertEqual(repr(a), "ConstContainer(30)")

        b = it.prev()
        self.assertEqual(repr(b), "ConstContainer(20)")

        c = it.prev()
        self.assertEqual(repr(c), "ConstContainer(10)")

        with self.assertRaises(StopIteration):
            it.prev()

    def test_forward_and_backward(self):
        it = ConstTwoDirIterator(self.items_str)

        self.assertEqual(repr(next(it)), "ConstContainer('A')")
        self.assertEqual(repr(next(it)), "ConstContainer('B')")

        self.assertEqual(repr(it.prev()), "ConstContainer('A')")

        self.assertEqual(repr(next(it)), "ConstContainer('B')")
        self.assertEqual(repr(next(it)), "ConstContainer('C')")

        with self.assertRaises(StopIteration):
            next(it)

    def test_start_position(self):
        it = ConstTwoDirIterator(self.items_int, start=-1)
        self.assertEqual(repr(next(it)), "ConstContainer(10)")

        it = ConstTwoDirIterator(self.items_int, start=0)
        self.assertEqual(repr(next(it)), "ConstContainer(20)")

        it = ConstTwoDirIterator(self.items_int, start=1)
        self.assertEqual(repr(next(it)), "ConstContainer(30)")

        it = ConstTwoDirIterator(self.items_int, start=2)
        with self.assertRaises(StopIteration):
            next(it)
