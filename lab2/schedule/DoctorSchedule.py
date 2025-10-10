from __future__ import annotations
from datetime import datetime, timedelta
from typing import List


class DoctorSchedule:
    def __init__(self, doctor: "Doctor"):
        self.doctor: "Doctor" = doctor
        self.talons: List["Talon"] = []

    def generate_week_talons(self, start_date: str):
        """Создать талоны на неделю (будни 8:00-20:00) через каждые 30 минут"""
        current_day = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = current_day + timedelta(days=7)

        while current_day < end_date:
            if current_day.weekday() < 5:  # только будни
                time_point = current_day.replace(hour=8, minute=0)
                end_time = current_day.replace(hour=20, minute=0)
                while time_point < end_time:
                    time_str = time_point.strftime("%H:%M")
                    self.talons.append(
                        Talon(current_day.strftime("%Y-%m-%d"), time_str, self.doctor)
                    )
                    time_point += timedelta(minutes=30)
            current_day += timedelta(days=1)

    def get_free_talons(self) -> list[Talon]:
        return [talon for talon in self.talons if not talon.is_taken]

    def book_talon(self, patient: Patient, date: str, time_str: str) -> Talon:
        """Записать пациента на конкретный талон"""
        for talon in self.talons:
            if talon.date == date and talon.time.strftime("%H:%M") == time_str:
                if talon.is_taken:
                    raise ValueError(f"Talon for {date} {time_str} is already taken")
                talon.add_an_appointment(patient)
                return talon
        raise ValueError(f"Talon for {date} {time_str} not found")

    def show_schedule(self) -> str:
        lines = []
        for talon in self.talons:
            status = f"занят ({talon.patient.name})" if talon.is_taken else "свободен"
            lines.append(f"{talon.date} {talon.time.strftime('%H:%M')} - {status}")
        return "\n".join(lines)
