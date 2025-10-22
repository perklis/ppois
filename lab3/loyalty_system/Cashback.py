class Cashback:
    def __init__(self, percent: float = 2.0):
        self.percent = percent

    def calculate(self, order_price: float):
        cashback_amount = order_price * (self.percent / 100)
        print(f"Cashback: {cashback_amount}")
        return cashback_amount

    def apply_to_card(self, loyalty_card, order_price: float):
        cashback_amount = self.calculate(order_price)
        loyalty_card.add_cashback(cashback_amount)
        print(f"Cashback applied to {loyalty_card.get_card_number()}")
