from employees.Employee import Employee
from security.SecurityReport import SecurityReport
from employees.Engineer import Engineer
from equipment.Equipment import Equipment


class SecurityGuard(Employee):
    def __init__(self, name: str, age: int, work_experience: int, shift_type: str):
        super().__init__("Security Guard", name, age, work_experience)
        self.shift_type = shift_type  # day / night
        self.__on_duty = False

    def start_shift(self) -> str:
        self.__on_duty = True
        return f"{self.name} started {self.shift_type} shift."

    def end_shift(self) -> str:
        self.__on_duty = False
        return f"{self.name} ended {self.shift_type} shift."

    def is_on_duty(self) -> bool:
        return self.__on_duty

    def report_incident(self, description: str) -> SecurityReport:
        report = SecurityReport(self.name, description)
        return report

    def notify_engineer(self, engineer: Engineer, equipment: Equipment) -> str:
        if equipment.condition == "Broken":
            return (
                f"{self.name} reported {equipment.name} to engineer {engineer.name}.\n"
                + engineer.repair_equipment(equipment)
            )
        return f"{equipment.name} is working fine, no report needed."

    def __str__(self):
        status = "on duty" if self.__on_duty else "off duty"
        return f"Security Guard {self.name}, {self.shift_type} shift ({status})"
