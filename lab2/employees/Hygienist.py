from employees.Employee import Employee
from employees.Orderly import Orderly


class Hygienist(Employee):
    def __init__(
        self,
        name: str,
        age: int,
        work_experience: int,
        materials_prepared: int = 0,
    ):
        super().__init__("Hygienist", name, age, work_experience)
        self._materials_prepared = materials_prepared
        self._trainings_conducted = 0
        self._last_training_topic = None
        self._trained_orderlies: list[Orderly] = []

    def conduct_training(self, topic: str, orderlies: list[Orderly]):
        self._last_training_topic = topic
        self._trainings_conducted += 1
        for orderly in orderlies:
            orderly.mark_trained(topic)
            self._trained_orderlies.append(orderly)
        print(f"{self.name} spoke about '{topic}' for {len(orderlies)} orderlies")

    def list_trained_orderlies(self) -> list[str]:
        return [orderly.name for orderly in self._trained_orderlies]
