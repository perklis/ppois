from orders.Order import Order
from exceptions import RatingTypeError


class CourierRating:
    def __init__(self, courier: "Courier"):
        self.courier = courier
        self.ratings = []

    def add_rating(self, order: Order, rating: float):
        if rating < 1 or rating > 5:
            raise RatingTypeError("Rating must be between 1 and 5")
        self.ratings.append(rating)
        print(f"Added rating {rating} for order #{order.order_number}")
        self._check_bonus()

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

    def _check_bonus(self):
        avg = self.get_average_rating()
        if avg > 4.0:
            self.courier.salary += 10
            print(
                f"Average rating {avg:.2f} > 4.0, {self.courier.name} gets 10 bonus. New salary: {self.courier.salary}"
            )
