from patients.Patient import Patient
from schedule.DoctorSchedule import DoctorSchedule
from employees.Employee import Employee
from typing import List
from exceptions import DoctorScheduleError


class Doctor(Employee):
    def __init__(
        self,
        job_title: str,
        name: str,
        age: int,
        work_experience: int,
        salary: float,
        specialisation: str,
        department: str,
    ):
        super().__init__(job_title, name, age, work_experience, salary)
        self.specialisation = specialisation
        self.department = department
        self._patients: List[Patient] = []
        self.schedule: DoctorSchedule | None = None

    def set_schedule(self, schedule: DoctorSchedule):
        if schedule.doctor != self:
            raise DoctorScheduleError("Schedule does not belong to this doctor")
        self.schedule = schedule

    def add_patient(self, patient: Patient):
        if patient not in self._patients:
            self._patients.append(patient)

    def add_diagnosis(
        self,
        patient: Patient,
        date: str,
        diagnosis: str,
        prescriptions: list[str] = None,
    ):
        if patient not in self._patients:
            raise DoctorScheduleError(
                f"Patient {patient.name} is not registered with Dr. {self.name}"
            )
        patient.medical_card.add_visit(date, self.name, diagnosis, prescriptions)

    def see_patient(
        self,
        patient: Patient,
        date: str,
        time_str: str,
        diagnosis: str,
        prescriptions: list[str] = None,
    ):
        if not self.schedule:
            raise DoctorScheduleError("Doctor hasn't schedule")
        talon = self.schedule.book_talon(patient, date, time_str)
        self.add_patient(patient)
        patient.medical_card.add_visit(date, self.name, diagnosis, prescriptions)

        return talon
