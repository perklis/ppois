from orders.Order import Order
from delivery.courier.Courier import Courier
from exceptions import EmptyOrderQueue


class OrderQueue:
    def __init__(self):
        self._queue: list[Order] = []

    def add_order(self, order: Order):
        self._queue.append(order)
        print(f"Order #{order.order_number} added to queue")

    def next_order(self, courier: Courier | None = None) -> Order | None:
        if not self._queue:
            raise EmptyOrderQueue("No orders in queue")
        order = self._queue.pop(0)
        if courier:
            courier.take_order(order.items)
        print(f"Order #{order.order_number} taken from queue")
        return order

    def list_orders(self):
        if not self._queue:
            raise EmptyOrderQueue("Queue is empty")
        print("Orders in queue:")
        for order in self._queue:
            print(f"Order #{order.order_number}")

    def count(self):
        return len(self._queue)
