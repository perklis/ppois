from employees.Employee import Employee
from typing import Optional
from patients.Patient import Patient


class Paramedic(Employee):
    def __init__(
        self, job_title: str, name: str, age: int, work_experience: int, salary: float
    ):
        super().__init__(job_title, name, age, work_experience, salary)
        self.ambulance: Optional["Ambulance"] = None

    def provide_first_aid(self, patient: Patient, symptoms: str):
        print(
            f"Paramedic {self.name} provided first aid to {patient.name} for {symptoms}"
        )
        if hasattr(patient, "medical_card"):
            patient.medical_card.add_visit(
                "Emergency", self.name, f"First aid for {symptoms}"
            )

    def transport_patient(self, patient: Patient, destination: str):
        print(f"Paramedic {self.name} is transporting {patient.name} to {destination}")
