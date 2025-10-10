from datetime import datetime

class Equipment:
    def __init__(self, name: str, serial_number: str, condition: str = "Working"):
        self.name = name
        self.serial_number = serial_number
        self.condition = condition  
        self.__last_checked_by = None

    def mark_checked(self, engineer_name: str):
        self.__last_checked_by = (engineer_name, datetime.now().strftime("%Y-%m-%d %H:%M"))
        return f"{self.name} checked by {engineer_name}"

    def repair(self):
        self.condition = "Working"
        return f"{self.name} repaired and now is working"

    def break_down(self):
        self.condition = "Broken"
        return f"{self.name} has broken down"

    def __str__(self):
        status = f"Condition: {self.condition}"
        if self.__last_checked_by:
            engineer, time = self.__last_checked_by
            status += f"Last checked by {engineer} at {time}"
        return f"{self.name} ({self.serial_number}) — {status}"
