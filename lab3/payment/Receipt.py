from __future__ import annotations
from datetime import datetime


class Receipt:
    _receipt_counter = 0

    def __init__(self, payment: "Payment"):
        Receipt._receipt_counter += 1
        self.receipt_number = Receipt._receipt_counter
        self.payment = payment
        self.created_at = datetime.now()

    def show(self):
        print(f"\nReceipt #{self.receipt_number}")
        print(f"Order: #{self.payment.order.order_number}")
        print(f"Amount: {self.payment.amount:.2f}")
        print(f"Method: {self.payment.paying_by.value}")
        if self.payment.tip:
            print(f"Tip: {self.payment.tip.amount:.2f}")
        print(f"Status: {self.payment.status.value}")
        print(f"Date: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
