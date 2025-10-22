from exceptions import NotEnoughInStock


class Inventory:
    def __init__(self):
        self.items: dict[str, int] = {}

    def add_item(self, name: str, quantity: int):
        self.items[name] = self.items.get(name, 0) + quantity
        print(f"Added {quantity} {name}, total {self.items[name]}")

    def use_item(self, name: str, quantity: int):
        if self.items.get(name, 0) < quantity:
            raise NotEnoughInStock(f"Not enough {name} in stock")
        self.items[name] -= quantity
        return True

    def get_quantity(self, name: str) -> int:
        return self.items.get(name, 0)

    def get_low_stock_items(self, threshold: int = 3) -> dict[str, int]:
        return {
            name: quantity
            for name, quantity in self.items.items()
            if quantity < threshold
        }
