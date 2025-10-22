from orders.Order import Order


class OrderList:
    def __init__(self):
        self.orders = []

    def add_order(self, order: Order):
        self.orders.append(order)
        print(f"Order #{order.order_number} added to courier list")

    def remove_order(self, order: Order):
        if order in self.orders:
            self.orders.remove(order)
            print(f"Order #{order.order_number} removed from courier list")

    def get_all_orders(self):
        return self.orders

    def count_orders(self):
        return len(self.orders)
