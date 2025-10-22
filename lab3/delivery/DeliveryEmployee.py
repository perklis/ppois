class DeliveryEmployee:
    def __init__(
        self,
        name: str,
        phone: str,
        salary: float,
        experience: int,
        department: str,
    ):
        self.name = name
        self.phone = phone
        self.salary = salary
        self.experience = experience
        self.department = department

        self.on_shift = False
        self.tasks_done = 0

    def start_shift(self):
        self.on_shift = True
        print(f"{self.name} started shift")

    def end_shift(self):
        self.on_shift = False
        print(f"{self.name} ended shift")

    def complete_task(self):
        self.tasks_done += 1
        print(f"{self.name} completed a task total {self.tasks_done}")

    def get_info(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"Phone: {self.phone}\n"
            f"Salary: {self.salary}\n"
            f"Experience: {self.experience} years\n"
            f"Department: {self.department}\n"
            f"On shift: {self.on_shift}\n"
            f"Tasks done: {self.tasks_done}"
        )

    def __str__(self):
        return f"{self.name}: ({self.department}), {self.experience} yrs exp"
