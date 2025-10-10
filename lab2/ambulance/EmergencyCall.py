from patients.Patient import Patient


class EmergencyCall:
    def __init__(self, patient: Patient, address: str, reason: str):
        self.patient = patient
        self.address = address
        self.reason = reason
        self.status = "pending"

    def accept(self):
        self.status = "accepted"
        print(f"Emergency call accepted for {self.patient.name}")

    def complete(self):
        self.status = "completed"
        print(f"Emergency call for {self.patient.name} completed")
