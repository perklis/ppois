from orders.Order import Order
from client.Client import Client
from datetime import datetime


class IssueReport:
    def __init__(self, order: Order, client: Client, description: str):
        self.order = order
        self.client = client
        self.description = description
        self.created_at = datetime.now()
        self.resolved = False
        print(
            f"Issue created for order #{self.order.order_number} by {self.client.name}"
        )

    def resolve(self):
        self.resolved = True
        print(f"Issue for order #{self.order.order_number} resolved")

    def show_issue(self):
        print(f"Issue for order #{self.order.order_number}")
        print(f"Client: {self.client.name}")
        print(f"Description: {self.description}")
        print(f"Created at: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Resolved: {self.resolved}")
