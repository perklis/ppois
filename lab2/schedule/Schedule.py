from datetime import datetime, timedelta
from schedule.Talon import Talon
from employees.Doctor import Doctor
from patients.Patient import Patient


class Schedule:
    def __init__(self):
        self.slots: list[Talon] = []

    def generate_week_slots(self, doctor: Doctor, start_date: str):
        current = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = current + timedelta(days=7)

        while current < end_date:
            if current.weekday() < 5:
                for hour in range(8, 20):
                    time_str = f"{hour:02d}:00"
                    self.slots.append(
                        Talon(current.strftime("%Y-%m-%d"), time_str, doctor)
                    )
            current += timedelta(days=1)

    def get_free_slots(self, doctor: Doctor = None) -> list[Talon]:
        result = [slot for slot in self.slots if not slot.booked]
        if doctor:
            result = [slot for slot in result if slot.doctor == doctor]
        return result

    def book_slot(
        self, patient: Patient, doctor: Doctor, date: str, time_str: str
    ) -> Talon:
        for slot in self.slots:
            if (
                slot.date == date
                and slot.time.strftime("%H:%M") == time_str
                and slot.doctor == doctor
            ):
                if slot.booked:
                    raise ValueError(
                        f"Талон {date} {time_str} у {doctor.name} уже занят"
                    )
                slot.book(patient)
                return slot
        raise ValueError(f"Талон на {date} {time_str} у {doctor.name} не найден")

    def get_doctor_schedule(self, doctor: Doctor) -> list[Talon]:
        return [s for s in self.slots if s.doctor == doctor]
