from typing import Optional
from ambulance.Paramedic import Paramedic
from ambulance.EmergencyCall import EmergencyCall


class Ambulance:
    def __init__(self, number: str, driver_name: str):
        self.number = number
        self.driver_name = driver_name
        self.paramedic: Optional[Paramedic] = None
        self.current_call: Optional[EmergencyCall] = None

    def assign_paramedic(self, paramedic: Paramedic):
        self.paramedic = paramedic
        paramedic.ambulance = self

    def receive_call(self, call: EmergencyCall):
        self.current_call = call
        print(f"Ambulance {self.number} is heading to {call.address}")

    def complete_call(self):
        if not self.current_call:
            print("No active emergency call")
            return
        print(
            f"Ambulance {self.number} completed call for {self.current_call.patient.name}"
        )
        self.current_call = None
