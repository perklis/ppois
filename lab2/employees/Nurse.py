from employees.Employee import Employee
from typing import Dict
from patients.Patient import Patient
from patients.Sickness import Sickness
from schedule.Talon import Talon
from laboratory.Laboratory import Laboratory


class Nurse(Employee):
    def __init__(
        self,
        job_title: str,
        name: str,
        age: int,
        work_experience: int,
        salary: float,
        department: str,
    ):
        super().__init__(job_title, name, age, work_experience, salary)
        self.department = department
        self._patient_records: Dict[Patient, list[dict]] = {}

    def _add_report(self, patient: Patient, report: dict):
        """Добавить отчёт по пациенту (внутренний учёт медсестры)."""
        if patient not in self._patient_records:
            self._patient_records[patient] = []
        self._patient_records[patient].append(report)

    def admit_patient(
        self,
        patient: Patient,
        sickness: Sickness,
        talon: Talon,
        pulse: int,
        blood_pressure: str,
        height: int,
        weight: int,
    ):
        """
        Медсестра принимает пациента, регистрирует данные и вносит запись в медкарту.
        """
        report = {
            "date": talon.date,
            "time": talon.time,
            "department": self.department,
            "diagnosis": sickness.name,
            "symptoms": ", ".join(sickness.symptoms),
            "severity": sickness.severity,
            "pulse": pulse,
            "blood_pressure": blood_pressure,
            "height": height,
            "weight": weight,
        }

        # Внутренняя запись медсестры
        self._add_report(patient, report)

        # Добавляем запись в медкарту пациента
        if patient.medical_card:
            patient.medical_card.add_visit(
                date=f"{talon.date} {talon.time}",
                doctor=self.name,  # если нет врача, можно указать медсестру
                diagnosis=sickness.name,
                prescriptions=[],
            )

        return f"Nurse {self.name} admitted patient {patient.name} for {sickness.name} on {talon.date} at {talon.time}."

    def write_referral(self, laboratory: Laboratory, patient: Patient, test_name: str):
        """
        Выдать направление на анализ — создаёт запись в лаборатории.
        """
        if patient not in self._patient_records:
            return f"Nurse {self.name} cannot issue referral: {patient.name} has not been admitted yet."

        laboratory.issue_referral(patient, test_name)
        return f"Nurse {self.name} issued referral for {patient.name} to {test_name}."

    def view_patient_reports(self, patient: Patient) -> str:
        """Посмотреть все записи по пациенту."""
        reports = self._patient_records.get(patient)
        if not reports:
            return f"No reports found for {patient.name}."
        formatted = "\n".join([str(r) for r in reports])
        return f"Reports for {patient.name}:\n{formatted}"
