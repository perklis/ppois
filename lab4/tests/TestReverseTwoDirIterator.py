import unittest
from task2.iters.ReverseTwoDirIterator import ReverseTwoDirIterator


class TestReverseTwoDirIterator(unittest.TestCase):
    def setUp(self):
        self.items_int = [10, 20, 30]
        self.items_str = ["A", "B", "C"]

    def test_reverse_forward_iteration(self):
        it = ReverseTwoDirIterator(self.items_int)

        self.assertEqual(next(it), 30)
        self.assertEqual(next(it), 20)
        self.assertEqual(next(it), 10)

        with self.assertRaises(StopIteration):
            next(it)

    def test_reverse_backward_iteration(self):
        it = ReverseTwoDirIterator(self.items_int, start_pos=0)

        self.assertEqual(it.prev(), 20)
        self.assertEqual(it.prev(), 30)

        with self.assertRaises(StopIteration):
            it.prev()

    def test_forward_and_backward_sequence(self):
        it = ReverseTwoDirIterator(self.items_str)

        self.assertEqual(next(it), "C")
        self.assertEqual(next(it), "B")
        self.assertEqual(it.prev(), "C")

        self.assertEqual(next(it), "B")
        self.assertEqual(next(it), "A")

        with self.assertRaises(StopIteration):
            next(it)

    def test_start_position(self):
        it = ReverseTwoDirIterator(self.items_int, start_pos=3)
        self.assertEqual(next(it), 30)

        it = ReverseTwoDirIterator(self.items_int, start_pos=2)
        self.assertEqual(next(it), 20)

        it = ReverseTwoDirIterator(self.items_int, start_pos=1)
        self.assertEqual(next(it), 10)

        it = ReverseTwoDirIterator(self.items_int, start_pos=0)
        with self.assertRaises(StopIteration):
            next(it)
