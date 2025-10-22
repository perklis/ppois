import unittest
from restaurant.kitchen.Shef import Shef
from restaurant.kitchen.Cook import Cook
from restaurant.FoodItem import FoodItem
from restaurant.Inventory import Inventory
from restaurant.kitchen.DishCategory import DishCategory


class TestShef(unittest.TestCase):
    def setUp(self):
        self.shef = Shef("Gordon", 1000, "123456789")
        self.cook1 = Cook("Jamie", 500, "987654321", "Italian")
        self.dish1 = FoodItem(
            "Pizza", 10.0, 500, {"Dough": 2, "Cheese": 1, "Tomato": 1}
        )
        self.dish2 = FoodItem("Pasta", 8.0, 400, {"Pasta": 2, "Sauce": 1})
        self.category = DishCategory("Italian")
        self.category.dishes = [self.dish1, self.dish2]
        self.inventory = Inventory()
        self.inventory.add_item("Dough", 10)
        self.inventory.add_item("Cheese", 5)
        self.inventory.add_item("Tomato", 5)
        self.inventory.add_item("Pasta", 10)
        self.inventory.add_item("Sauce", 5)

    def test_add_cook_and_signature_dish(self):
        self.shef.add_cook(self.cook1)
        self.assertIn(self.cook1, self.shef.team)

        self.shef.add_signature_dish(self.dish1)
        self.assertIn(self.dish1, self.shef.signature_dishes)

    def test_plan_menu(self):
        self.shef.plan_menu([self.category])

    def test_check_inventory(self):
        self.shef.check_inventory(self.inventory)
        self.inventory.use_item("Dough", 9)
        self.shef.check_inventory(self.inventory)
