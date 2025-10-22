import unittest
from unittest.mock import Mock
from restaurant.Picker import Picker
from delivery.courier.Courier import Courier
from exceptions import DishesNotFoundError, OrderNotFound


class TestPicker(unittest.TestCase):
    def setUp(self):
        self.picker = Picker("Alice", 1000, "123456789")
        self.dish1 = Mock(name="Dish1")
        self.dish1.name = "Pizza"
        self.dish2 = Mock(name="Dish2")
        self.dish2.name = "Soup"
        self.courier = Mock(spec=Courier)
        self.courier.name = "Bob"

    def test_take_dish_from_cook(self):
        self.picker.take_dish_from_cook(self.dish1)
        self.assertIn(self.dish1, self.picker.collected_dishes)

    def test_make_order_package_success(self):
        self.picker.take_dish_from_cook(self.dish1)
        self.picker.take_dish_from_cook(self.dish2)
        order = self.picker.make_order_package()
        self.assertEqual(order, [self.dish1, self.dish2])
        self.assertEqual(len(self.picker.collected_dishes), 0)
        self.assertEqual(len(self.picker.ready_orders), 1)

    def test_make_order_package_no_dishes_raises(self):
        with self.assertRaises(DishesNotFoundError):
            self.picker.make_order_package()

    def test_give_to_courier_success(self):
        self.picker.take_dish_from_cook(self.dish1)
        self.picker.make_order_package()
        self.picker.give_to_courier(self.courier)
        self.assertEqual(self.picker.tasks_done, 1)
        self.assertEqual(len(self.picker.ready_orders), 0)
        self.courier.take_order.assert_called_once_with([self.dish1])

    def test_give_to_courier_no_orders_raises(self):
        with self.assertRaises(OrderNotFound):
            self.picker.give_to_courier(self.courier)

    def test_show_ready_orders(self):
        self.picker.take_dish_from_cook(self.dish1)
        self.picker.make_order_package()
        self.picker.show_ready_orders()
