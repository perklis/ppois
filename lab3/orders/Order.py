from __future__ import annotations
from typing import List
from datetime import datetime

from orders.OrderItem import OrderItem
from orders.OrderStatus import OrderStatus
from delivery.DeliveryZone import DeliveryZone
from payment.Payment import Payment
from payment.PaymentBy import PaymentBy
from exceptions import AdressNotInDeliveryZone


class Order:
    _order_counter: int = 0

    def __init__(self, client):
        self.client = client
        self.items: List[OrderItem] = []
        self.status: OrderStatus = OrderStatus.PROCESSING
        self.created_at: datetime = datetime.now()
        self.delivered_at: datetime | None = None
        self.payment: Payment | None = None

        Order._order_counter += 1
        self.order_number: int = Order._order_counter

        delivery_zone = DeliveryZone()
        address = client._address
        if not delivery_zone.is_in_zone(address):
            raise AdressNotInDeliveryZone(
                f"Delivery not available for address '{address.full_address()}'"
            )

        print(f"Delivery available for {address.full_address()}")
        print(f"Order #{self.order_number} created for {self.client.name}")

    def add_item(self, order_item: OrderItem) -> None:
        if order_item.quantity <= 0:
            print("Cannot add item with zero or negative quantity")
            return
        self.items.append(order_item)
        print(
            f"Added {order_item.food_item.name} x{order_item.quantity} to order #{self.order_number}"
        )

    def remove_item(self, dish_name: str) -> None:
        before = len(self.items)
        self.items = [item for item in self.items if item.food_item.name != dish_name]
        if len(self.items) < before:
            print(f"Removed {dish_name} from order #{self.order_number}")
        else:
            print(f"{dish_name} not found in order #{self.order_number}")

    def get_total_price(self) -> float:
        return round(sum(item.get_total_price() for item in self.items), 2)

    def change_status(self, new_status: OrderStatus) -> None:
        if new_status not in OrderStatus:
            print("Invalid order status")
            return

        self.status = new_status
        print(f"Order #{self.order_number} status changed to {self.status}")

        if new_status == OrderStatus.DELIVERED:
            self.delivered_at = datetime.now()
            print(
                f"Order #{self.order_number} delivered at {self.delivered_at.strftime('%Y-%m-%d %H:%M:%S')}"
            )

    def pay(self, method: PaymentBy = PaymentBy.CARD) -> Payment | None:
        if not self.items:
            print("Cannot pay for an empty order.")
            return None

        if self.payment is not None:
            print(f"Order #{self.order_number} already paid.")
            return self.payment

        amount = self.get_total_price()
        self.payment = Payment(self, amount, method)
        self.payment.process()

        if hasattr(self.payment, "is_successful") and self.payment.is_successful():
            self.change_status(OrderStatus.READY)

        return self.payment

    def show_order(self) -> None:
        print(f"\nOrder #{self.order_number} for {self.client.name}")
        if not self.items:
            print("No items in order.")
        else:
            for item in self.items:
                print(item)
        print(f"Total: {self.get_total_price()}")
        print(f"Status: {self.status}")
        print(f"Created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        if self.delivered_at:
            print(f"Delivered: {self.delivered_at.strftime('%Y-%m-%d %H:%M:%S')}")
        if self.payment:
            print("Payment info:")
            self.payment.show_summary()
