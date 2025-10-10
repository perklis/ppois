from employees.Employee import Employee
from employees.base_salaries import BASE_SALARIES
from typing import List


class Economist(Employee):
    def __init__(
        self,
        name: str,
        age: int,
        work_experience: int,
        department: str,
        monthly_budget=60000,
    ):
        super().__init__("Economist", name, age, work_experience)
        self.department = department
        self.monthly_budget = monthly_budget
        self.processed_employees: List[Employee] = []

    def calculate_salary(self, employee: Employee) -> float:
        """Рассчитать зарплату одного сотрудника"""
        base_salary = BASE_SALARIES.get(employee.job_title, 800)
        new_salary = base_salary + 50 * employee.work_experience
        employee._set_salary(new_salary)
        return new_salary

    def adjust_salaries_to_budget(self, employees: List[Employee]):
        """Если суммарные зарплаты превышают бюджет, уменьшаем зарплаты на 1% по этапам"""
        total = sum(self.calculate_salary(emp) for emp in employees)
        self.processed_employees = employees.copy()

        iteration = 0
        while total > self.monthly_budget:
            iteration += 1
            for emp in employees:
                reduced_salary = emp.salary * 0.99
                emp._set_salary(reduced_salary)
            total = sum(emp.salary for emp in employees)
            if iteration > 100:  # защита от бесконечного цикла
                break

        print(
            f"{self.name} adjusted salaries to fit the budget: {self.monthly_budget}. Total after adjustment: {total}"
        )

    def calculate_all_salaries(self, employees: List[Employee]) -> float:
        """Расчёт всех зарплат с учётом бюджета"""
        for emp in employees:
            self.calculate_salary(emp)
        total_salaries = sum(emp.salary for emp in employees)

        if total_salaries > self.monthly_budget:
            self.adjust_salaries_to_budget(employees)
            total_salaries = sum(emp.salary for emp in employees)

        return total_salaries
