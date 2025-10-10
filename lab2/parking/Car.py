from dataclasses import dataclass


@dataclass
class Car:
    owner_type: str
    owner_name: str
    color: str
    number: str
