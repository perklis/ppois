from employees.Employee import Employee
from employees.ProcurementSpecialist import ProcurementSpecialist
from typing import List


class Clerk(Employee):
    def __init__(
        self,
        name: str,
        age: int,
        work_experience: int,
        salary: float,
        department: str,
        tasks: List[str] = None,
        handled_documents: int = 0,
    ):
        super().__init__("Clerk", name, age, work_experience, salary)
        self.department = department
        self.tasks = tasks or []
        self.handled_documents = handled_documents

    def assign_task(self, task: str):
        self.tasks.append(task)
        print(f"Task '{task}' assigned to {self.name}")

    def complete_task(self, task: str):
        if task in self.tasks:
            self.tasks.remove(task)
            self.handled_documents += 1
            print(f"{self.name} completed task '{task}'")
        else:
            print(f"Task '{task}' not found for {self.name}")

    def receive_report(self, specialist: ProcurementSpecialist):
        """Получить отчет от специалиста по закупкам напрямую от объекта"""
        report = specialist.generate_report()
        print(f"Report received by {self.name}:\n{report}")
