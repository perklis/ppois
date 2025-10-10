from patients.Patient import Patient
from employees.Doctor import Doctor
from patients.Sickness import Sickness


class EmergencyRoom:
    def __init__(self, room_number: int, doctor: Doctor):
        self.room_number = room_number
        self.doctor = doctor
        self.current_patient: Patient | None = None

    def admit_patient(self, patient: Patient, reason: str):
        self.current_patient = patient
        print(f"Patient {patient.name} admitted to ER {self.room_number} for {reason}")

    def diagnose_and_treat(self, diagnosis: str, severity: str):
        if not self.current_patient:
            print("No patient in the ER.")
            return
        if (
            not hasattr(self.current_patient, "medical_card")
            or self.current_patient.medical_card is None
        ):
            raise AttributeError(
                f"Patient {self.current_patient.name} has no medical card"
            )

        sickness = Sickness(diagnosis, ["pain", "fever"], severity)
        self.current_patient.medical_card.add_sickness(sickness)
        self.doctor.add_patient(self.current_patient)
        self.doctor.add_diagnosis(self.current_patient, "Emergency", diagnosis)
        print(
            f"Doctor {self.doctor.name} treated {self.current_patient.name} for {diagnosis}"
        )
        self.current_patient = None
