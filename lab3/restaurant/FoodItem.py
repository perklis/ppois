from __future__ import annotations
from typing import Optional
from exceptions import NotEnoughInStock


class FoodItem:
    def __init__(
        self,
        name: str,
        price: float,
        ingredients: dict[str, int],
        calories: int,
        category: Optional["DishCategory"] = None,
    ):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.calories = calories
        self.category = category
        self.is_available = True

        if category:
            category.add_dish(self)

    def get_info(self) -> str:
        category_name = self.category.name if self.category else "No category"
        ingredient_str = ", ".join(f"{k}({v})" for k, v in self.ingredients.items())
        return f"{self.name}: {category_name}\nPrice {self.price}, ccal: {self.calories}\nIngredients {ingredient_str}"

    def check_availability(self, inventory: "Inventory") -> bool:
        for ingredient, quantity in self.ingredients.items():
            if inventory.get_quantity(ingredient) < quantity:
                self.is_available = False
                raise NotEnoughInStock(f"Not enough {ingredient} for {self.name}")
        self.is_available = True
        print(f"All ingredients for {self.name} are available")
        return True

    def cook(self, inventory: "Inventory") -> bool:
        if not self.check_availability(inventory):
            print(f"Cannot cook {self.name}")
            return False
        for ingreds, quantity in self.ingredients.items():
            inventory.use_item(ingreds, quantity)
        print(f"{self.name} is cooked")
        return True
