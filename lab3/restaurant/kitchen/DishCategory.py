from __future__ import annotations
from typing import List


class DishCategory:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.dishes: List["FoodItem"] = []

    def add_dish(self, dish: "FoodItem"):
        if dish not in self.dishes:
            self.dishes.append(dish)
            dish.category = self
            print(f"Added {dish.name} to {self.name}")

    def remove_dish(self, dish_name: str):
        before = len(self.dishes)
        self.dishes = [d for d in self.dishes if d.name != dish_name]
        if len(self.dishes) < before:
            print(f"Removed {dish_name} from {self.name}")

    def list_dishes(self):
        print(f"Category {self.name}")
        for d in self.dishes:
            print(f"{d.name} {d.price}")

    def get_average_price(self) -> float:
        if not self.dishes:
            return 0
        return round(sum(d.price for d in self.dishes) / len(self.dishes), 2)

    def get_most_expensive_dish(self) -> "FoodItem" | None:
        if not self.dishes:
            return None
        most_expensive = self.dishes[0]
        for dish in self.dishes[1:]:
            if dish.price > most_expensive.price:
                most_expensive = dish
        return most_expensive
