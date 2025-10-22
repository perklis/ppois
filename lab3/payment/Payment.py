from __future__ import annotations
from datetime import datetime
from typing import Optional

from payment.Transaction import Transaction
from payment.Tip import Tip
from payment.PaymentBy import PaymentBy
from payment.PaymentStatus import PaymentStatus


class Payment:
    def __init__(
        self, order: str = "Order", amount: float = 0.0, paying_by: PaymentBy = None
    ):
        self.order = order
        self.amount: float = amount
        self.paying_by: PaymentBy = paying_by
        self.status: PaymentStatus = PaymentStatus.PENDING
        self.created_at: datetime = datetime.now()
        self.transaction: Optional[Transaction] = None
        self.receipt: Optional["Receipt"] = None
        self.tip: Optional[Tip] = None

    def process(self):
        try:
            self.transaction = Transaction(self.amount, self.paying_by)
            self.transaction.execute()

            from payment.Receipt import Receipt

            self.receipt = Receipt(self)

            self.status = PaymentStatus.COMPLETED
            print(f"Payment #{self.order.order_number} completed successfully")
        except Exception as e:
            self.status = PaymentStatus.FAILED
            print(f"Payment failed for order #{self.order.order_number}: {e}")

    def add_tip(self, amount: float):
        if self.status != PaymentStatus.COMPLETED:
            print("Cannot add tip before payment completion")
            return
        self.tip = Tip(amount)
        print(f"Tip of {amount:.2f} added for order #{self.order.order_number}")

    def refund(self):
        if self.status != PaymentStatus.COMPLETED:
            print("Can't refund an uncompleted payment")
            return
        self.status = PaymentStatus.REFUNDED
        print(f"Payment for order #{self.order.order_number} refunded")

    def show_summary(self):
        print(f"Order #{self.order.order_number}")
        print(f"Amount: {self.amount:.2f}")
        print(f"Paid by: {self.paying_by.value}")
        print(f"Status: {self.status.value}")
        print(f"Created at: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        if self.tip:
            print(f"Tip: {self.tip.amount:.2f}")
        if self.receipt:
            print(
                f"Receipt issued at: {self.receipt.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
            )

    def is_successful(self):
        return self.status == PaymentStatus.COMPLETED
