from __future__ import annotations
from datetime import datetime
from typing import Optional
from exceptions import TalonTakingError  # оставляем кастомное исключение


class Talon:
    def __init__(self, date: str, time_str: str, doctor: "Doctor"):
        self.date = date
        self.time = datetime.strptime(time_str, "%H:%M").time()
        self.doctor: "Doctor" = doctor
        self.patient: Optional["Patient"] = None
        self.is_taken = False

    def add_an_appointment(self, patient: "Patient"):
        if self.is_taken:
            raise TalonTakingError(
                f"Talon for {self.date} {self.time.strftime('%H:%M')} doctor: {self.doctor.name} is taken"
            )
        self.patient = patient
        self.is_taken = True

    def __repr__(self):
        status = "is taken" if self.is_taken else "is free"
        patient_name = self.patient.name if self.patient else "free"
        return f"{self.date} {self.time.strftime('%H:%M')}\nDoctor: {self.doctor.name}\nPatient:{patient_name} [{status}]"
