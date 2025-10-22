from delivery.courier.Courier import Courier
from orders.Order import Order
from delivery.DeliveryEstimator import DeliveryEstimator


class Delivery:
    def __init__(self):
        self.couriers: list[Courier] = []
        self.orders_in_progress: list[Order] = []
        self.estimator = DeliveryEstimator()

    def add_courier(self, courier: Courier):
        self.couriers.append(courier)
        print(f"Courier {courier.name} added to delivery")

    def assign_order(self, order: Order):
        courier = self.estimator.assign_courier(order, self.couriers)
        if courier:
            courier.take_order(order.items)
            self.orders_in_progress.append(order)
        else:
            print(f"Order #{order.order_number} is waiting for courier")

    def complete_order(self, courier: Courier, customer_rating: float = None):
        if not courier.current_order:
            print(f"{courier.name} has no current order")
            return
        courier.deliver_order(customer_rating=customer_rating)
        if courier.current_order in self.orders_in_progress:
            self.orders_in_progress.remove(courier.current_order)
