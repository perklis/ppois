from restaurant.FoodItem import FoodItem
from restaurant.Inventory import Inventory
from restaurant.RestaurantEmployee import RestaurantEmployee
from restaurant.kitchen.Cook import Cook
from restaurant.kitchen.DishCategory import DishCategory


class Shef(RestaurantEmployee):
    def __init__(self, name: str, salary: float, phone: str):
        super().__init__(name, salary, phone, position="Shef")
        self.signature_dishes = []
        self.team = []

    def add_cook(self, cook: "Cook"):
        self.team.append(cook)
        print(f"Added {cook.name} to team")

    def add_signature_dish(self, dish: "FoodItem"):
        self.signature_dishes.append(dish)
        print(f"Added signature dish {dish.name}")

    def plan_menu(self, categories: list["DishCategory"]):
        print(f"Menu by {self.name}")
        for cat in categories:
            print(f"{cat.name}")
            for dish in cat.dishes:
                print(f"{dish.name} {dish.price}")

    def check_inventory(self, inventory: "Inventory"):
        low = inventory.get_low_stock_items()
        if low:
            print(f"Low stock {', '.join(low.keys())}")
        else:
            print("Inventory is full")
