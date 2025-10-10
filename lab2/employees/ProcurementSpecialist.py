# employees/ProcurementSpecialistPharmacy.py
from employees.Employee import Employee
from pharmacy.Pharmacy import Pharmacy
from pharmacy.Medication import Medication
from typing import List, Dict, Union


class ProcurementSpecialist(Employee):
    def __init__(
        self,
        name: str,
        age: int,
        work_experience: int,
        salary: float,
        department: str,
    ):
        super().__init__("Procurement Specialist", name, age, work_experience, salary)
        self.department = department
        self.purchases: List[Dict[str, Union[str, int]]] = []

    def monthly_procurement(self, pharmacy: Pharmacy):
        for pharmacist in pharmacy.pharmacists:
            inventory = pharmacist.inventory
            for med_name in inventory._medications.keys():
                self._order_medication(inventory, med_name, 40)
            common_meds = ["Paracetamol", "Ibuprofen", "Acyclovir"]
            for med_name in common_meds:
                if med_name not in inventory._medications:
                    self._order_medication(inventory, med_name, 40)

    def _order_medication(self, inventory, med_name: str, quantity: int):
        current_qty = inventory.get_quantity(med_name)
        inventory.add_medication(Medication(med_name, quantity))
        self.purchases.append({"item": med_name, "quantity": quantity})
        print(
            f"{self.name} ordered {quantity} units of {med_name} (current stock: {current_qty})"
        )

    def generate_report(self) -> str:
        if not self.purchases:
            return f"{self.name} has not made any purchases yet"
        report_lines = [f"{self.name}'s procurement report:"]
        for purchase in self.purchases:
            report_lines.append(f"{purchase['item']}: {purchase['quantity']} units")
        return "\n".join(report_lines)
