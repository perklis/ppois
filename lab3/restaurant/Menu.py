from __future__ import annotations
from typing import List
from restaurant.FoodItem import FoodItem
from restaurant.kitchen.DishCategory import DishCategory


class Menu:
    def __init__(self):
        self.categories: List[DishCategory] = []
        self.items: List[FoodItem] = []

    def add_category(self, category: DishCategory):
        if category not in self.categories:
            self.categories.append(category)
            print(f"Added category {category.name}")

    def add_item(self, item: FoodItem):
        if item not in self.items:
            self.items.append(item)
            if item.category and item.category not in self.categories:
                self.add_category(item.category)
            print(f"Added item {item.name}")

    def remove_item(self, name: str):
        before = len(self.items)
        self.items = [i for i in self.items if i.name != name]
        if len(self.items) < before:
            print(f"Removed {name} from menu")

    def find_by_category(self, category_name: str) -> List[FoodItem]:
        result = [
            i for i in self.items if i.category and i.category.name == category_name
        ]
        print(f"{len(result)} items in {category_name}")
        return result

    def find_by_price(self, min_price: float, max_price: float) -> List[FoodItem]:
        result = [i for i in self.items if min_price <= i.price <= max_price]
        print(f"{len(result)} items in price range")
        return result

    def get_available_items(self) -> List[FoodItem]:
        result = [i for i in self.items if i.is_available]
        print(f"{len(result)} items available")
        return result

    def show_menu(self):
        print("Menu")
        for cat in self.categories:
            print(f"\n{cat.name}")
            for dish in cat.dishes:
                print(f"{dish.name} {dish.price}")
