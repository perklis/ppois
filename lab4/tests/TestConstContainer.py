import unittest
from task2.iters.ConstContainer import ConstContainer
from task2.exceptions import ConstContainerEditingError


class TestConstContainer(unittest.TestCase):
    def setUp(self):
        class Dummy:
            def __init__(self):
                self.x = 42
                self.y = "hello"

        self.obj = Dummy()
        self.container = ConstContainer(self.obj)

    def test_getattribute_success(self):
        self.assertEqual(self.container.x, 42)
        self.assertEqual(self.container.y, "hello")

    def test_getattribute_missing_attr(self):
        with self.assertRaises(ConstContainerEditingError):
            _ = self.container.z

    def test_getattribute_wrapped_blocked(self):
        with self.assertRaises(ConstContainerEditingError):
            _ = self.container._wrapped

    def test_setattr_blocked(self):
        with self.assertRaises(ConstContainerEditingError):
            self.container.x = 100
