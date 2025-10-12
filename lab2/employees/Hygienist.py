from employees.Employee import Employee
from employees.Orderly import Orderly
from typing import List


class Hygienist(Employee):
    def __init__(
        self,
        name: str,
        age: int,
        work_experience: int,
        salary: float,
        materials_prepared: int = 0,
    ):
        super().__init__("Hygienist", name, age, work_experience, salary)
        self._materials_prepared = materials_prepared
        self._trainings_conducted = 0
        self._last_training_topic = None
        self._trained_orderlies: List[Orderly] = []

    def conduct_training(self, topic: str, orderlies: List[Orderly]):
        self._last_training_topic = topic
        self._trainings_conducted += 1
        for orderly in orderlies:
            orderly.mark_trained(topic, instructor_name=self.name)
            self._trained_orderlies.append(orderly)
        print(f"{self.name} spoke about '{topic}' for {len(orderlies)} orderlies")

    def list_trained_orderlies(self) -> List[str]:
        return [orderly.name for orderly in self._trained_orderlies]

    def __str__(self):
        return (
            f"Hygienist {self.name}, prepared materials: {self._materials_prepared}, "
            f"trainings conducted: {self._trainings_conducted}"
        )
