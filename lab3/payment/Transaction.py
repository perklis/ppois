from datetime import datetime
from payment.PaymentBy import PaymentBy


class Transaction:
    _id_counter = 0

    def __init__(self, amount: float, paying_by: PaymentBy):
        Transaction._id_counter += 1
        self.transaction_id = Transaction._id_counter
        self.amount = amount
        self.paying_by = paying_by
        self.time = None
        self.successful = False

    def execute(self):
        self.time = datetime.now()
        self.successful = True
        print(
            f"Transaction #{self.transaction_id} executed ({self.paying_by}) for {self.amount}"
        )
