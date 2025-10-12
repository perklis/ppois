from typing import Optional
from datetime import date
from patients.MedicalCard import MedicalCard


class Patient:
    def __init__(
        self,
        name: str,
        address: str,
        phone_number: str,
        workplace: str,
        birth_year: int,
    ):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.workplace = workplace
        self.birth_year = birth_year
        self.__medical_card: Optional[MedicalCard] = None
        self.__assigned_doctor = None

    @property
    def medical_card(self):
        return self.__medical_card

    def assign_medical_card(self, card: MedicalCard):
        from patients.MedicalCard import MedicalCard

        if not isinstance(card, MedicalCard):
            raise TypeError("MedicalCard instance required")
        self.__medical_card = card

    def get_medical_card(self):
        if not self.__medical_card:
            raise ValueError(f"Patient {self.name} doesn't have a medical card")
        return self.__medical_card

    def assign_doctor(self, doctor):
        from employees.Doctor import Doctor

        if not isinstance(doctor, Doctor):
            raise TypeError("Assigned doctor must be of type Doctor")
        self.__assigned_doctor = doctor

    def calculate_age(self) -> int:
        return date.today().year - self.birth_year

    def __str__(self):
        return (
            f"Patient {self.name}, {self.calculate_age()} y.o.\n"
            f"Address: {self.address}\n"
            f"Phone: {self.phone_number}\n"
            f"Workplace: {self.workplace}"
        )
