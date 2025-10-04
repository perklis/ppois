from dataclasses import dataclass
from Employee import Employee
from typing import List, Dict

@dataclass
class Doctor(Employee):
    cabinet_number:int
    specialisation: str
    department: str
    _patients: List[Doctor.patients]=[]
    
    def add_patient(self, patient_name:str, diagnosis:str, addres:str)
