from delivery.DeliveryEmployee import DeliveryEmployee
from exceptions import OrderNotFound
from delivery.courier.CourierRating import CourierRating


class Courier(DeliveryEmployee):
    def __init__(self, name: str, phone: str, salary: float):
        super().__init__(name, phone, salary, experience=0, department="Delivery")
        self.current_order = None
        self.status = "waiting"
        self.order_list = []
        self.rating = CourierRating(self)
        self.vehicle = None

    def take_order(self, order_items):
        self.current_order = order_items
        self.status = "delivering"
        print(f"{self.name} took order with {len(order_items)} dishes")

    def check_order_status(self):
        if not self.current_order:
            raise OrderNotFound("No current order")
        dish_names = [d.food_item.name for d in self.current_order]
        print(f"Current order ready with dishes {dish_names}")

    def deliver_order(self, address: str, customer_rating: float = None):
        if not self.current_order:
            raise OrderNotFound("No order to deliver")

        print(f"{self.name} delivered {len(self.current_order)} dishes to {address}")
        self.salary += 5
        print(f"{self.name} earned 5 salary bonus, new salary {self.salary}")

        self.order_list.append(self.current_order[0].order)

        if customer_rating is not None:
            self.rating.add_rating(self.current_order[0].order, customer_rating)

        self.current_order = None
        self.status = "waiting"
