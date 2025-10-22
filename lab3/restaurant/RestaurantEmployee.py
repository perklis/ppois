class RestaurantEmployee:
    def __init__(self, name: str, salary: float, phone: str, position: str):
        self.name = name
        self.salary = salary
        self.phone = phone
        self.position = position
        self.hours_worked = 0

    def work(self):
        print(f"{self.name} is working")

    def log_hours(self, hours: int):
        self.hours_worked += hours
        print(f"{self.name} worked {hours} hours {self.hours_worked}")

    def give_raise(self, percent: float):
        if percent > 0:
            self.salary += self.salary * (percent / 100)
            print(f"{self.name} got a raise new salary {self.salary}")

    def get_info(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"Position: {self.position}\n"
            f"Salary: {self.salary}\n"
            f"Phone: {self.phone}"
        )
