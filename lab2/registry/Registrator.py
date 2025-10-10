from employees.Employee import Employee
from patients.Patient import Patient
from registry.MedicalCardsArchive import MedicalCardsArchive
from patients.MedicalCard import MedicalCard
from schedule.DoctorSchedule import DoctorSchedule
from schedule.AppointmentQueue import AppointmentQueue


class Registrator(Employee):
    def __init__(
        self,
        name: str,
        age: int,
        work_experience: int,
        salary: float,
        archive: MedicalCardsArchive,
    ):
        super().__init__("Registrator", name, age, work_experience, salary)
        self.archive = archive

    def register_patient(
        self,
        patient: Patient,
        doctor_schedule: DoctorSchedule,
        queue: AppointmentQueue,
        date: str,
        time_str: str,
    ) -> MedicalCard:
        medcard = MedicalCard(patient)
        self.archive._add_card(medcard)

        talon = doctor_schedule.book_talon(patient, date, time_str)

        queue.add_talon(talon)
        return medcard
