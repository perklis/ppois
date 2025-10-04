from Employee import Employee
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Nurse(Employee):
    department: str

    def _add_report(self, patient_name: str, report: Dict[str, str]):
        if patient_name not in self.patient_records:
            self.patient_records[patient_name] = []
        self.patient_records[patient_name].append(report)

    def fill_in_admission_details(self, patient_name: str, symptoms: str, pulse: int, 
        patient_pressure: str, diagnosis: str, height:int, weight:int):
        report = {
            "department": self.department,
            "symptoms": symptoms,
            "pulse": str(pulse),
            "blood_pressure": patient_pressure,
            "diagnosis": diagnosis,
            "height": height,
            "weight": weight
        }
        self._add_report(patient_name, report)
        return f"Nurse {self.name} from department of {self.department}) recorded admission details for {patient_name}"
