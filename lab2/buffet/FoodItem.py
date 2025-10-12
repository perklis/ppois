from exceptions import NotEnoughItemError


class FoodItem:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def reduce_quantity(self, amount: int):
        if amount > self.quantity:
            raise NotEnoughItemError(f"Not enough {self.name}")
        self.quantity -= amount

    def add_quantity(self, amount: int):
        self.quantity += amount

    def __repr__(self):
        return f"{self.name} - {self.quantity} pcs for {self.price}₽"
