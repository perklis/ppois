from typing import List
from schedule.Talon import Talon
from patients.Patient import Patient


class AppointmentQueue:
    def __init__(self):
        self.queue: List[Talon] = []

    def add_talon(self, talon: Talon):
        if not talon.is_taken:
            raise ValueError("This talon is free")
        self.queue.append(talon)
        self.queue.sort(key=lambda t: (t.date, t.time))

    def get_next_patient(self) -> Patient | None:
        if self.queue:
            return self.queue[0].patient
        return None

    def pop_next_patient(self) -> Patient | None:
        if self.queue:
            return self.queue.pop(0).patient
        return None

    def remove_patient(self, patient: Patient):
        self.queue = [talon for talon in self.queue if talon.patient != patient]

    def show_queue(self) -> str:
        lines = [
            f"{talon.date} {talon.time.strftime('%H:%M')} - {talon.patient.name}"
            for talon in self.queue
        ]
        return "\n".join(lines)
