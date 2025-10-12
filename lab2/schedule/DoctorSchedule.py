from __future__ import annotations
from datetime import datetime, timedelta
from typing import List
from exceptions import TalonTakingError  # кастомное исключение


class DoctorSchedule:
    def __init__(self, doctor: "Doctor"):
        self.doctor: "Doctor" = doctor
        self.talons: List["Talon"] = []

    def generate_week_talons(self, start_date: str):
        from schedule.Talon import (
            Talon,
        )  # локальный импорт для предотвращения кругового импорта

        current_day = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = current_day + timedelta(days=7)

        while current_day < end_date:
            if current_day.weekday() < 5:  # только будние дни
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

    def book_talon(self, patient: "Patient", date: str, time_str: str) -> "Talon":
        for talon in self.talons:
            if talon.date == date and talon.time.strftime("%H:%M") == time_str:
                if talon.is_taken:
                    raise TalonTakingError(
                        f"Talon for {date} {time_str} is already taken"
                    )
                talon.add_an_appointment(patient)
                return talon
        raise TalonTakingError(f"Talon for {date} {time_str} not found")

    def get_talon(self, patient, date: str, time_str: str):
        """
        Возвращает талон для данного пациента, даты и времени, не бронируя его.
        """
        for talon in self.talons:
            if talon.date == date and talon.time.strftime("%H:%M") == time_str:
                return talon
        raise TalonTakingError(f"Talon for {date} {time_str} not found")

    def show_schedule(self) -> str:
        lines = []
        for talon in self.talons:
            status = f"is taken ({talon.patient.name})" if talon.is_taken else "free"
            lines.append(f"{talon.date} {talon.time.strftime('%H:%M')} - {status}")
        return "\n".join(lines)
