from laboratory.LabTest import LabTest
from employees.Laborant import Laborant

class Laboratory:
    def __init__(self):
        self.available_tests = [
            LabTest("Blood Test", "< 50", "g/L"),
            LabTest("Cholesterol", "< 200", "mg/dL"),
            LabTest("Glucose", "< 100", "mg/dL")
        ]
        self.__valid_referrals: dict[str, list[str]] = {}  # {patient_name: [tests]}
        self.laborants: list[Laborant] = []

    def add_laborant(self, laborant: Laborant):
        self.laborants.append(laborant)

    def issue_referral(self, patient_name: str, test_name: str):
        """Выдать направление (обычно от медсестры)"""
        if patient_name not in self.__valid_referrals:
            self.__valid_referrals[patient_name] = []
        self.__valid_referrals[patient_name].append(test_name)

    def check_referral(self, patient_name: str, test_name: str) -> bool:
        """Проверить, есть ли направление"""
        return test_name in self.__valid_referrals.get(patient_name, [])

    def get_test_by_name(self, test_name: str):
        for test in self.available_tests:
            if test.test_name == test_name:
                return test
        raise ValueError(f"Test '{test_name}' not found")

    def perform_analysis(self, laborant: Laborant, patient, test_name: str):
        """Провести анализ, если есть направление"""
        if not self.check_referral(patient.name, test_name):
            return f"No valid referral for {patient.name} to {test_name}"

        test = self.get_test_by_name(test_name)
        return laborant.perform_test(patient, test)
