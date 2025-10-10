from random import randint
from patients.Analysis import Analysis


class LabResult:
    def __init__(
        self,
        patient_name: str,
        card_number: str,
        test_name: str,
        normal_range: str,
        units: str,
    ):
        self.patient_name = patient_name
        self.card_number = card_number
        self.test_name = test_name
        self.normal_range = normal_range
        self.units = units
        self.value = randint(10, 100)
        self.result_text = self._compare_result_and_norm()

    def _compare_result_and_norm(self) -> str:
        try:
            limit = int(self.normal_range.split()[-1])
            status = "Normal" if self.value <= limit else "Above normal"
        except:
            status = "Impossible to identify"
        return f"{self.test_name}: {self.value} {self.units} ({status})"

    def to_analysis(self, doctor_name: str, date: str) -> Analysis:
        return Analysis(self.test_name, self.result_text, doctor_name, date)

    def __str__(self):
        return (
            f"Patient {self.patient_name}\nCard: {self.card_number}: {self.result_text}"
        )
