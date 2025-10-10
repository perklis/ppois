from employees.Employee import Employee
from pharmacy.Inventory import Inventory
from pharmacy.Medication import Medication


class Pharmacist(Employee):
    def __init__(self, name: str, age: int, work_experience: int, salary: float):
        super().__init__("Pharmacist", name, age, work_experience, salary)
        self._inventory = Inventory()

    def check_stock(self, medication_name: str) -> str:
        qty = self._inventory.get_quantity(medication_name)
        return f"{medication_name}: {qty} pcs in stock"

    def dispense_medication(self, medication_name: str, quantity: int) -> str:
        if self._inventory.get_quantity(medication_name) < quantity:
            return f"Not enough {medication_name} in stock"
        self._inventory.remove_medication(medication_name, quantity)
        return f"{quantity} pcs of {medication_name} dispensed"

    def add_medication(self, medication: Medication) -> str:
        self._inventory.add_medication(medication)
        return f"{medication.quantity} pcs of {medication.name} added to inventory"

    def generate_inventory_report(self) -> str:
        meds = [
            f"{m.name}: {m.quantity} {m.unit}"
            for m in self._inventory._medications.values()
        ]
        if not meds:
            return "Inventory is empty"
        return "Inventory Report:\n" + "\n".join(meds)
