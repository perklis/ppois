from dataclasses import dataclass
from Employee import Employee

@dataclass
class Registrator(Employee):
    reception_number: int
    record_counts: int
# че нить с подбором медикал кард на день