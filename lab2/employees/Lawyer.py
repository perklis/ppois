from employees.Employee import Employee


class Lawyer(Employee):
    def __init__(self, name: str, age: int, work_experience: int, salary: float):
        super().__init__("Lawyer", name, age, work_experience, salary)
        self.__cases = []  # список юридических дел
        self.__complaints = []  # жалобы пациентов/персонала

    def add_case(self, case_description: str) -> str:
        """Добавить новое юридическое дело"""
        self.__cases.append(case_description)
        return f"Case added: {case_description}"

    def add_complaint(self, complaint: str) -> str:
        """Добавить жалобу"""
        self.__complaints.append(complaint)
        return f"Complaint recorded: {complaint}"

    def _generate_report(self) -> dict:
        """Возвращает сводный отчёт по юридическим вопросам"""
        return {"cases": self.__cases.copy(), "complaints": self.__complaints.copy()}
