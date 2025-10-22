from orders.Order import Order


class QueueBeforeOrder:
    def __init__(self):
        self._orders: list[Order] = []

    def add_order(self, order: Order):
        self._orders.append(order)
        print(f"Order #{order.order_number} added to queue")

    def count_before(self, order: Order) -> int:
        if order not in self._orders:
            print(f"Order #{order.order_number} not found in queue")
            return 0
        index = self._orders.index(order)
        count = index
        print(f"{count} orders before order #{order.order_number}")
        return count

    def remove_order(self, order: Order):
        if order in self._orders:
            self._orders.remove(order)
            print(f"Order #{order.order_number} removed from queue")

    def get_all_orders(self) -> list[Order]:
        return list(self._orders)
