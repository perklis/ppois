from buffet.FoodItem import FoodItem


class FoodStock:
    def __init__(self):
        self.items: dict[str, FoodItem] = {}

    def add_item(self, item: FoodItem):
        if item.name in self.items:
            self.items[item.name].add_quantity(item.quantity)
        else:
            self.items[item.name] = item

    def sell_item(self, item: FoodItem, quantity: int) -> float:
        if item.name not in self.items:
            raise ValueError(f"{item.name} not in stock")
        stock_item = self.items[item.name]
        if quantity > stock_item.quantity:
            raise ValueError(f"Not enough {item.name}")
        stock_item.reduce_quantity(quantity)
        if stock_item.quantity == 0:
            del self.items[item.name]
        return stock_item.price * quantity

    def check_stock(self, item: FoodItem, quantity: int) -> bool:
        return item.name in self.items and self.items[item.name].quantity >= quantity

    def show_low_stock(self) -> str:
        return "\n".join(
            str(item) for item in self.items.values() if item.quantity <= 3
        )
