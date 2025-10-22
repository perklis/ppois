from restaurant.RestaurantEmployee import RestaurantEmployee
from exceptions import CleaningError


class Cleaner(RestaurantEmployee):
    def __init__(self, name: str, salary: float, phone: str):
        super().__init__(name, salary, phone, position="Cleaner")
        self.cleaned_rooms = 0
        self.tools_ready = True

    def clean_room(self, room_name: str):
        if not self.tools_ready:
            raise CleaningError(f"{self.name} can't clean tools not ready")
        self.cleaned_rooms += 1
        print(f"{self.name} cleaned {room_name}")

    def prepare_tools(self):
        self.tools_ready = True
        print(f"{self.name} prepared tools")

    def report(self):
        print(f"{self.name} cleaned {self.cleaned_rooms} rooms")

    def take_break(self):
        print(f"{self.name} is taking short break")
