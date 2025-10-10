from employees.Employee import Employee
from equipment.Equipment import Equipment


class Engineer(Employee):
    def __init__(
        self,
        name: str,
        age: int,
        work_experience: int,
        specialization: str,
        department: str,
    ):
        super().__init__("Engineer", name, age, work_experience)
        self.specialization = specialization
        self.department = department
        self.__equipment_list: list[Equipment] = []

    def add_equipment(self, equipment: Equipment) -> str:
        if not isinstance(equipment, Equipment):
            raise TypeError("Only Equipment objects can be added")
        if equipment not in self.__equipment_list:
            self.__equipment_list.append(equipment)
            return f"Engineer {self.name} is now responsible for {equipment.name}"
        return f"Engineer {self.name} already maintains {equipment.name}"

    def check_equipment(self, equipment: Equipment) -> str:
        if equipment not in self.__equipment_list:
            return f"{self.name} isn't assigned to {equipment.name}"
        return equipment.mark_checked(self.name)

    def repair_equipment(self, equipment: Equipment) -> str:
        if equipment not in self.__equipment_list:
            return f"{self.name} can't repair {equipment.name}"
        if equipment.condition == "Working":
            return f"{equipment.name} is already working"
        return equipment.repair()

    def list_equipment(self) -> str:
        if not self.__equipment_list:
            return f"{self.name} has no assigned equipment"
        return "\n".join(str(eq) for eq in self.__equipment_list)

    def __str__(self):
        return (
            f"Engineer {self.name}, specialization: {self.specialization}, "
            f"department: {self.department},amount of equipment: {len(self.__equipment_list)}"
        )
