from restaurant.RestaurantEmployee import RestaurantEmployee
from restaurant.FoodItem import FoodItem
from restaurant.Inventory import Inventory


class Cook(RestaurantEmployee):
    def __init__(self, name: str, salary: float, phone: str, specialization: str):
        super().__init__(name, salary, phone, position="Cook")
        self.specialization = specialization
        self.dishes_prepared = 0

    def prepare_dish(self, dish: FoodItem, inventory: Inventory):
        if dish.cook(inventory):
            self.dishes_prepared += 1
            print(f"{self.name} cooked {dish.name}")
            return True
        return False

    def report(self):
        print(f"{self.name} cooked {self.dishes_prepared} dishes")
