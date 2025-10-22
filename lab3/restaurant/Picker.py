from restaurant.RestaurantEmployee import RestaurantEmployee
from restaurant.FoodItem import FoodItem
from exceptions import OrderNotFound, DishesNotFoundError


class Picker(RestaurantEmployee):
    def __init__(self, name: str, salary: float, phone: str):
        super().__init__(name, salary, phone, position="Picker")
        self.collected_dishes: list[FoodItem] = []
        self.ready_orders: list[list[FoodItem]] = []
        self.tasks_done: int = 0

    def take_dish_from_cook(self, dish: FoodItem):
        self.collected_dishes.append(dish)
        print(f"{self.name} took {dish.name} from cook")

    def make_order_package(self):
        if not self.collected_dishes:
            raise DishesNotFoundError("No dishes to pack")
        order = self.collected_dishes.copy()
        self.collected_dishes.clear()
        self.ready_orders.append(order)
        print(f"{self.name} packed one order")
        return order

    def give_to_courier(self, courier: "Courier"):
        if not self.ready_orders:
            raise OrderNotFound("No orders to give")
        for order in self.ready_orders:
            courier.take_order(order)
        print(f"{self.name} gave {len(self.ready_orders)} orders to {courier.name}")
        self.tasks_done += len(self.ready_orders)
        self.ready_orders.clear()

    def show_ready_orders(self):
        print(f"{self.name} ready orders {len(self.ready_orders)}")
        for i, order in enumerate(self.ready_orders, 1):
            print(f"Order {i}: {[dish.name for dish in order]}")
