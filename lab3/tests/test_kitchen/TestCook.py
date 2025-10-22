import unittest
from restaurant.kitchen.Cook import Cook
from restaurant.FoodItem import FoodItem
from restaurant.Inventory import Inventory
from exceptions import NotEnoughInStock


class TestCook(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.inventory.add_item("Dough", 5)
        self.inventory.add_item("Cheese", 3)
        self.inventory.add_item("Tomato", 2)

        self.pizza = FoodItem("Pizza", 10.0, "Main", 500)
        self.pizza.ingredients = {"Dough": 2, "Cheese": 1, "Tomato": 1}

        self.cook = Cook("Marina", 1000, "123456789", "Italian")

    def test_prepare_dish_success(self):
        result = self.cook.prepare_dish(self.pizza, self.inventory)
        self.assertTrue(result)
        self.assertEqual(self.inventory.get_quantity("Dough"), 3)
        self.assertEqual(self.inventory.get_quantity("Cheese"), 2)
        self.assertEqual(self.inventory.get_quantity("Tomato"), 1)
        self.assertEqual(self.cook.dishes_prepared, 1)

    def test_prepare_dish_insufficient_ingredients(self):
        self.inventory.use_item("Dough", 5)
        with self.assertRaises(NotEnoughInStock):
            self.cook.prepare_dish(self.pizza, self.inventory)

    def test_report_prints(self):
        self.cook.prepare_dish(self.pizza, self.inventory)
        self.assertEqual(self.cook.dishes_prepared, 1)
        self.cook.report()
