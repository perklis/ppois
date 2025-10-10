from typing import List
from employees.SecurityGuard import SecurityGuard
from security.SecurityReport import SecurityReport


class SecurityDepartment:
    def __init__(self, department_name: str):
        self.department_name = department_name
        self.__guards: List[SecurityGuard] = []
        self.__reports: List[SecurityReport] = []

    def add_guard(self, guard: SecurityGuard) -> str:
        if not isinstance(guard, SecurityGuard):
            raise TypeError("Only SecurityGuard objects can be added")
        if guard in self.__guards:
            return f"{guard.name} already works in the department"
        self.__guards.append(guard)
        return f"{guard.name} added to {self.department_name}"

    def remove_guard(self, guard: SecurityGuard) -> str:
        if guard in self.__guards:
            self.__guards.remove(guard)
            return f"{guard.name} removed from {self.department_name}"
        return f"{guard.name} is not found in {self.department_name}"

    def get_on_duty_guards(self) -> List[SecurityGuard]:
        return [g for g in self.__guards if g.is_on_duty()]

    def collect_report(self, report: SecurityReport):
        if not isinstance(report, SecurityReport):
            raise TypeError("Only SecurityReport objects can be collected")
        self.__reports.append(report)

    def show_all_reports(self) -> str:
        if not self.__reports:
            return f"No incidents reported in {self.department_name}"
        return "\n".join(str(r) for r in self.__reports)

    def assign_shift(self, guard: SecurityGuard, shift_type: str) -> str:
        if guard not in self.__guards:
            return f"{guard.name} is not part of {self.department_name}"
        guard.shift_type = shift_type
        return f"{guard.name} assigned to {shift_type} shift"

    def __str__(self):
        return (f"Security Department: {self.department_name}\n"
                f"Total guards: {len(self.__guards)}\n"
                f"On duty: {len(self.get_on_duty_guards())}\n"
                f"Total reports: {len(self.__reports)}")
