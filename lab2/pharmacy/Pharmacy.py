from employees.Pharmacist import Pharmacist
from pharmacy.Medication import Medication
from typing import List
from exceptions import NoPharmacistAssignedError, NotEnoughItemError


class Pharmacy:
    def __init__(self, name: str):
        self.name = name
        self.pharmacists: List[Pharmacist] = []

    def hire_pharmacist(self, pharmacist: Pharmacist):
        self.pharmacists.append(pharmacist)

    def list_pharmacists(self) -> List[str]:
        return [p.name for p in self.pharmacists]

    def add_medication_to_inventory(self, medication: Medication) -> str:
        if not self.pharmacists:
            raise NoPharmacistAssignedError(
                "No pharmacists available to add medication"
            )
        return self.pharmacists[0].add_medication(medication)

    def dispense_to_patient(self, medication_name: str, quantity: int) -> str:
        if not self.pharmacists:
            raise NoPharmacistAssignedError(
                "No pharmacists available to dispence medication"
            )
        for pharmacist in self.pharmacists:
            result = pharmacist.dispense_medication(medication_name, quantity)
            if "dispensed" in result:
                return result
        raise NotEnoughItemError(
            f"Unable to dispense {medication_name}, not enough stock"
        )

    def check_medication_stock(self, medication_name: str) -> str:
        if not self.pharmacists:
            raise NoPharmacistAssignedError(
                "No pharmacists available to check med stock"
            )
        return self.pharmacists[0].check_stock(medication_name)
