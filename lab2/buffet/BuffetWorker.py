from employees.Employee import Employee
from patients.Patient import Patient
from buffet.FoodItem import FoodItem
from buffet.FoodStock import FoodStock


class BuffetWorker(Employee):
    def __init__(self, name: str, age: int, experience: int, salary: float):
        super().__init__("BuffetWorker", name, age, experience, salary)
        self.sales_total = 0

    def sell_food(
        self, stock: FoodStock, patient: Patient, item: FoodItem, quantity: int
    ):
        if not stock.check_stock(item, quantity):
            raise ValueError(f"Not enough {item.name}")
        price = stock.sell_item(item, quantity)
        self.sales_total += price
        print(
            f"{self.name} sells {quantity} {item.name} to patient {patient.name} price: {round(price, 2)}₽"
        )
        return price
