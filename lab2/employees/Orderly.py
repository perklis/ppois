from employees.Employee import Employee
from typing import List, Optional
from schedule.CleaningSchedule import CleaningSchedule


class Orderly(Employee):
    def __init__(
        self,
        name: str,
        age: int,
        work_experience: int,
        salary: float,
        equipment_list: Optional[List[str]] = None,
    ):
        super().__init__("Orderly", name, age, work_experience, salary)
        self.assigned_rooms: List[str] = []
        self.schedule: Optional[CleaningSchedule] = None
        self.equipment_list = equipment_list if equipment_list else []
        self._trained_topics: List[str] = []
        self._last_instructor: Optional[str] = None

    def assign_schedule(self, schedule: CleaningSchedule):
        self.schedule = schedule
        schedule.add_orderly(self)

    def assign_room(self, room_number: str):
        if room_number not in self.assigned_rooms:
            self.assigned_rooms.append(room_number)
            if self.schedule:
                self.schedule.add_room(room_number)

    def perform_cleaning(
        self, room_number: str, required_equipment: Optional[List[str]] = None
    ):
        required_equipment = required_equipment if required_equipment else []
        missing_equipment = [
            eq for eq in required_equipment if eq not in self.equipment_list
        ]
        if missing_equipment:
            print(
                f"{self.name} cannot clean room {room_number}. Missing equipment: {', '.join(missing_equipment)}"
            )
            return
        if room_number not in self.assigned_rooms:
            print(f"{self.name} is not assigned to room {room_number}")
            return
        print(
            f"{self.name} is cleaning room {room_number} using: {', '.join(self.equipment_list)}"
        )
        if self.schedule:
            self.schedule.mark_cleaned(room_number, self)

    def mark_trained(self, topic: str, instructor_name: Optional[str] = None):
        """Called by HygieneInstructor — marks training completion."""
        self._trained_topics.append(topic)
        self._last_instructor = instructor_name
        print(
            f"{self.name} completed hygiene training on '{topic}'"
            + (f" (Instructor: {instructor_name})" if instructor_name else "")
        )

    def get_training_info(self) -> str:
        if not self._trained_topics:
            return f"{self.name} has not completed any hygiene training yet."
        topics = ", ".join(self._trained_topics)
        return f"{self.name} has completed training on: {topics}."
