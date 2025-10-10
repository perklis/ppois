from buffet.FoodItem import FoodItem
from buffet.FoodStock import FoodStock
from buffet.BuffetWorker import BuffetWorker
from patients.Patient import Patient


class Buffet:
    def __init__(self, stock: FoodStock, worker: BuffetWorker):
        self.stock = stock
        self.worker = worker

    def sell_to_patient(self, patient: Patient, item: FoodItem, quantity: int):
        return self.worker.sell_food(self.stock, patient, item, quantity)

    def check_stock(self, item: FoodItem, quantity: int) -> bool:
        return self.stock.check_stock(item, quantity)

    def show_low_stock(self) -> str:
        return self.stock.show_low_stock()
