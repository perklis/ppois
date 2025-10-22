from datetime import datetime
from delivery_support.IssueReport import IssueReport
from orders.Order import Order
from client.Client import Client
from exceptions import RatingInputError


class Review:
    def __init__(self, order: Order, client: Client, rating: int, comment: str = ""):
        if order.status != "DELIVERED" and str(order.status) != "OrderStatus.DELIVERED":
            print(
                f"Cannot review order #{order.order_number} because i's not delivered"
            )
            raise ValueError("Order not delivered")

        if rating < 1 or rating > 5:
            raise RatingInputError("Rating must be between 1 and 5")

        self.order = order
        self.client = client
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()
        self.issue: IssueReport | None = None

        print(
            f"Review added for order #{self.order.order_number} by {self.client.name} with rating {self.rating}"
        )

        if rating < 5:
            self.create_issue()

    def create_issue(self):
        description = self.comment if self.comment else "No comment provided"
        self.issue = IssueReport(self.order, self.client, description)
