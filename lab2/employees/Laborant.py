from employees.Employee import Employee
from laboratory.LabResult import LabResult
from laboratory.LabTest import LabTest
from datetime import date


class Laborant(Employee):
    def __init__(self, name: str, age: int, work_experience: int, salary: float):
        super().__init__("Laborant", name, age, work_experience, salary)
        self.completed_tests: list[LabResult] = []

    def perform_test(self, patient, lab_test: LabTest):
        card = patient.get_medical_card()
        result = LabResult(
            patient.name,
            card.card_number,
            lab_test.test_name,
            lab_test.normal_range,
            lab_test.units,
        )
        self.completed_tests.append(result)

        analysis = result.to_analysis(self.name, date.today().strftime("%Y-%m-%d"))
        card.add_analysis(analysis)

        return f"Analysis for {patient.name} ({lab_test.test_name}) are done"

    def list_completed_tests(self):
        if not self.completed_tests:
            return "No tests performed yet"
        return "\n".join(str(r) for r in self.completed_tests)
