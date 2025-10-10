from __future__ import annotations
from typing import Dict, List, Optional


class CleaningSchedule:
    def __init__(self):
        self.schedule: Dict[
            str, Optional["Orderly"]
        ] = {}  # {room_number: last_cleaned_by}
        self.orderlies: List["Orderly"] = []

    def add_orderly(self, orderly: "Orderly"):
        if orderly not in self.orderlies:
            self.orderlies.append(orderly)

    def add_room(self, room_number: str):
        if room_number not in self.schedule:
            self.schedule[room_number] = None

    def mark_cleaned(self, room_number: str, orderly: "Orderly"):
        if room_number in self.schedule:
            self.schedule[room_number] = orderly
            print(f"Room {room_number} marked as cleaned by {orderly.name}")
