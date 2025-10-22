from orders.Order import Order


class RestaurantAnalytics:
    def __init__(self):
        self.orders: list[Order] = []

    def record_order(self, order: Order):
        self.orders.append(order)
        print(f"Order #{order.order_number} recorded")

    def total_revenue(self) -> float:
        total = 0
        for order in self.orders:
            total += order.get_total_price()
        print(f"Total revenue: {total}")
        return total

    def most_popular_dishes(self) -> dict:
        counter = {}
        for order in self.orders:
            for item in order.items:
                counter[item.food_item.name] = (
                    counter.get(item.food_item.name, 0) + item.quantity
                )
        sorted_counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
        print("Most popular dishes:", sorted_counter)
        return sorted_counter
