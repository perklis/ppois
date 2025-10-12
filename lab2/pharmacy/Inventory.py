from pharmacy.Medication import Medication
from exceptions import NotEnoughItemError, ItemNotFound


class Inventory:
    def __init__(self):
        self._medications: dict[str, Medication] = {}

    def add_medication(self, medication: Medication):
        if medication.name in self._medications:
            self._medications[medication.name].quantity += medication.quantity
        else:
            self._medications[medication.name] = medication

    def remove_medication(self, medication_name: str, quantity: int):
        if medication_name not in self._medications:
            raise ItemNotFound(f"Medication {medication_name} not found")
        if self._medications[medication_name].quantity < quantity:
            raise NotEnoughItemError(f"Not enough {medication_name} in stock")
        self._medications[medication_name].quantity -= quantity
        if self._medications[medication_name].quantity == 0:
            del self._medications[medication_name]

    def get_quantity(self, medication_name: str) -> int:
        return self._medications.get(
            medication_name, Medication(medication_name, 0)
        ).quantity
