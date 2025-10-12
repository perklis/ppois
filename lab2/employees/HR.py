from employees.Employee import Employee
from employees.Doctor import Doctor
from employees.HeadPhysician import HeadPhysician


class HR(Employee):
    def __init__(
        self,
        name: str,
        age: int,
        work_experience: int,
        salary: float,
        total_employees: int = 0,
    ):
        super().__init__("HR Specialist", name, age, work_experience, salary)
        self.__total_employees = total_employees

    @property
    def count_all_employees(self):
        return self.__total_employees

    def hire_employee(self, new_employee: Employee):
        if isinstance(new_employee, (Doctor, HeadPhysician)):
            raise PermissionError("Only Head Physician can hire doctors")
        self.__total_employees += 1
        return f"HR {self.name} hired {new_employee.job_title} {new_employee.name}"

    def fire_employee(self, employee: Employee):
        if isinstance(employee, (Doctor, HeadPhysician)):
            raise PermissionError("HR cannot fire doctors or Head Physician")
        self.__total_employees = max(0, self.__total_employees - 1)
        return f"HR {self.name} fired {employee.job_title} {employee.name}"

    def make_interview(
        self, candidate_name: str, candidate_age: int, candidate_experience: int
    ):
        if candidate_age < 20:
            return f"Candidate {candidate_name} is too young for employment"
        if candidate_experience < 2:
            return f"Candidate {candidate_name} has insufficient experience"
        return f"Candidate {candidate_name} passed the interview"

    def __str__(self):
        return f"HR {self.name}\nexperience: {self.work_experience} years"
