from orders.Order import Order
from delivery.courier.Courier import Courier
from exceptions import CouriersNotFound
from client.Weather import Weather
from orders.QueueBeforeOrder import QueueBeforeOrder


class DeliveryEstimator:
    def __init__(self):
        self.weather = Weather()
        self.queue = QueueBeforeOrder()

    def estimate_time(self, order: Order) -> int:
        time = 10 + len(order.items) * 5
        print(f"Estimated delivery time for order #{order.order_number}: {time} min")
        return time

    def estimate_cost(self, order: Order) -> float:
        cost = 3 + len(order.items) * 1.5

        city = order.client._address.city
        current_weather = self.weather.get_weather(city)
        if current_weather.lower() in ("snow", "rain"):
            cost *= 1.03
            print(f"Weather in {city}: {current_weather} cost increased by 3%")

        orders_before = self.queue.count_before(order)
        if orders_before > 10:
            cost *= 0.98
            print(
                f"There are {orders_before} orders before #{order.order_number}"
                f"Delivery cost decreased by 2%"
            )

        cost = round(cost, 2)
        print(f"Estimated delivery cost for order #{order.order_number}: {cost}")
        return cost

    def assign_courier(self, order: Order, couriers: list[Courier]) -> Courier | None:
        available = [c for c in couriers if c.on_shift and c.status == "waiting"]
        if not available:
            raise CouriersNotFound("No available courier")

        selected = available[0]
        for c in available[1:]:
            if c.salary < selected.salary:
                selected = c

        print(f"Order #{order.order_number} assigned to {selected.name}")
        return selected
