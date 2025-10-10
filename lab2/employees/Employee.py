class Employee:
    def __init__(
        self, job_title: str, name: str, age: int, work_experience: int, salary: float
    ):
        self.job_title = job_title
        self.name = name
        self.age = age
        self.work_experience = work_experience
        self.__salary = 0.0

    def get_information(self) -> str:
        return (
            f"{self.__class__.__name__}:\nPosition: {self.job_title}\n"
            f"Name: {self.name}\nAge: {self.age}\n"
            f"Work length: {self.work_experience} years"
        )

    def add_experience(self, years: int = 1):
        self.work_experience += years
        return f"Work expirience {self.name} increases to {self.work_experience} years"

    def get_salary(self) -> float:
        return self.__salary

    def _set_salary(self, value: float):
        self.__salary = value
