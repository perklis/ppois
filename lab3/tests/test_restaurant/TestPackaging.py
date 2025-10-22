import unittest
from restaurant.Packaging import Packaging
from restaurant.kitchen.DishCategory import DishCategory


class TestPackaging(unittest.TestCase):
    def setUp(self):
        self.packaging = Packaging()
        self.drink_category = DishCategory("Soft Drink")
        self.soup_category = DishCategory("Tomato Soup")
        self.pizza_category = DishCategory("Pizza Margarita")
        self.misc_category = DishCategory("Salad")

    def test_choose_packaging(self):
        self.packaging.choose_packaging(self.drink_category)
        self.assertEqual(self.packaging.type_name, "Cup")
        self.assertEqual(self.packaging.material, "Plastic")

        self.packaging.choose_packaging(self.soup_category)
        self.assertEqual(self.packaging.type_name, "Bowl")
        self.assertEqual(self.packaging.material, "Paper")

        self.packaging.choose_packaging(self.pizza_category)
        self.assertEqual(self.packaging.type_name, "Box")
        self.assertEqual(self.packaging.material, "Cardboard")

        self.packaging.choose_packaging(self.misc_category)
        self.assertEqual(self.packaging.type_name, "Container")
        self.assertEqual(self.packaging.material, "Plastic")

    def test_pack_dish_ready(self):
        result = self.packaging.pack_dish("Pizza Margarita", self.pizza_category)
        self.assertTrue(result)
        self.assertTrue(self.packaging.is_used)

    def test_pack_dish_not_ready(self):
        self.packaging.is_ready = False
        result = self.packaging.pack_dish("Pizza Margarita", self.pizza_category)
        self.assertFalse(result)
        self.assertFalse(self.packaging.is_used)

    def test_prepare_resets_packaging(self):
        self.packaging.is_ready = False
        self.packaging.is_used = True
        self.packaging.prepare()
        self.assertTrue(self.packaging.is_ready)
        self.assertFalse(self.packaging.is_used)

    def test_mark_used_sets_flags(self):
        self.packaging.mark_used()
        self.assertFalse(self.packaging.is_ready)
        self.assertTrue(self.packaging.is_used)

    def test_get_info_returns_correct_string(self):
        self.packaging.type_name = "Box"
        self.packaging.material = "Cardboard"
        self.packaging.is_ready = True
        self.packaging.is_used = False
        info = self.packaging.get_info()
        expected = "Type: Box\nMaterial: Cardboard\nReady: True\nUsed: False"
        self.assertEqual(info, expected)
