class Tip:
    def __init__(self, amount: float):
        if amount < 0:
            raise ValueError("Tip can't be negative")
        self.amount = amount
