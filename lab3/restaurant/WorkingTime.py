class WorkingTime:
    def __init__(self, restaurant_name: str):
        self.restaurant_name = restaurant_name
        self.open_hour = 9
        self.close_hour = 21

    def is_open(self, hour: int) -> bool:
        open_status = self.open_hour <= hour < self.close_hour
        print(f"Restaurant {self.restaurant_name} is open: {open_status}")
        return open_status

    def set_hours(self, open_hour: int, close_hour: int):
        self.open_hour = open_hour
        self.close_hour = close_hour
        print(
            f"{self.restaurant_name} working hours set {self.open_hour}:00 - {self.close_hour}:00"
        )
