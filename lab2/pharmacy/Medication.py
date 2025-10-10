from dataclasses import dataclass


@dataclass
class Medication:
    name: str
    quantity: int
    unit: str = "pcs"
    expiration_date: str = "N/A"
