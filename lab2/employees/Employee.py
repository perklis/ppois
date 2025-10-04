from dataclasses import dataclass

@dataclass
class Employee:
    job_title: str
    name: str
    age: int
    work_experience: int

    def get_information(self) -> str:
        return f"{self.__class__.__name__}:\n Position:{self.job_title} {self.name}, Age: {self.age}, Work length: {self.work_experience}"
