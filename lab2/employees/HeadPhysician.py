from employees.Employee import Employee
from employees.Doctor import Doctor
from employees.Economist import Economist
from typing import List
from employees.Lawyer import Lawyer
from security.SecurityDepartment import SecurityDepartment


class HeadPhysician(Employee):
    def __init__(self, job_title, name, age, work_experience, salary):
        super().__init__(job_title, name, age, work_experience, salary)
        self.__doctors: list[Doctor] = []

    def list_doctors(self) -> List[str]:
        return [doc.name for doc in self.__doctors]

    def get_doctor_schedule(self, doctor: Doctor) -> List[str]:
        if doctor not in self.__doctors:
            raise PermissionError(f"Doctor {doctor.name} is not in staff")
        if not doctor.schedule:
            return []
        return doctor.schedule.show_schedule().split("\n")

    def request_patient_report(self, doctor: Doctor, medical_card_number: str):
        if doctor not in self.__doctors:
            raise PermissionError(f"Doctor {doctor.name} is not in staff")
        for patient in doctor._patients:
            if patient.medical_card.card_number == medical_card_number:
                return patient.medical_card.get_visits()
        raise ValueError("There isn't this patient")

    def request_weekly_patient_cards(self, registrator):
        return registrator.get_weekly_cards()

    def give_bonus_to_employees(
        self, economist: Economist, threshold=15000, bonus_percent=3
    ):
        for employee in economist.get_all_employees():
            if employee.get_salary() < threshold:
                bonus = employee.get_salary() * (bonus_percent / 100)
                employee._set_salary(employee.get_salary() + bonus)

    def request_security_report(self, security_department: SecurityDepartment) -> str:
        if not isinstance(security_department, SecurityDepartment):
            raise TypeError("Expected SecurityDepartment instance")
        return security_department.show_all_reports()

    def request_legal_report(self, lawyer: Lawyer):
        if not isinstance(lawyer, Lawyer):
            raise TypeError("Expected Lawyer instance")
        print(f"Head Physician {self.name} requested a report from {lawyer.name}")
        return lawyer._generate_report()
