from __future__ import annotations
from restaurant.FoodItem import FoodItem


class OrderItem:
    def __init__(
        self,
        food_item: FoodItem,
        quantity: int = 1,
        order: "Order" | None = None,
    ):
        self.food_item = food_item
        self.quantity = quantity
        self.order = order

    def get_total_price(self) -> float:
        return round(self.food_item.price * self.quantity, 2)

    def __str__(self):
        return f"{self.food_item.name} x{self.quantity} = {self.get_total_price()}"
