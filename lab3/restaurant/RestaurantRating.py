from orders.Order import Order


class RestaurantRating:
    def __init__(self):
        self.ratings: list[float] = []

    def add_rating(self, order: Order, value: float):
        if 1 <= value <= 5:
            self.ratings.append(value)
            print(f"Added rating {value} for order #{order.order_number}")
        else:
            print("Rating must be between 1 and 5")

    def average_rating(self) -> float:
        if not self.ratings:
            return 0.0
        avg = sum(self.ratings) / len(self.ratings)
        return round(avg, 2)
