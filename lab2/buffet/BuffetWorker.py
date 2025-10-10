from employees.Employee import Employee
from patients.Patient import Patient
from buffet.FoodItem import FoodItem
from buffet.FoodStock import FoodStock


class BuffetWorker(Employee):
    """Буфетчик без скидок, работает с объектами FoodItem"""

    def __init__(self, name: str, age: int, experience: int, salary: float):
        super().__init__("BuffetWorker", name, age, experience, salary)
        self.sales_total = 0

    def sell_food(
        self, stock: FoodStock, patient: Patient, item: FoodItem, quantity: int
    ):
        if not stock.check_stock(item, quantity):
            raise ValueError(f"Недостаточно {item.name} на складе")
        price = stock.sell_item(item, quantity)
        self.sales_total += price
        print(
            f"{self.name} продал {quantity} {item.name} пациенту {patient.name} за {round(price, 2)}₽"
        )
        return price
