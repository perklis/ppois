from employees.Employee import Employee
from parking.Parking import Parking
from parking.Car import Car
from typing import Optional


class ParkingWorker(Employee):
    def __init__(
        self,
        name: str,
        age: int,
        work_experience: int,
        salary: float,
        parking_lot: Parking,
    ):
        super().__init__("Parking Workwr", name, age, work_experience, salary)
        self._parking_lot: Parking = parking_lot
        self._current_car: Optional[Car] = None
        self._cars_served_today: int = 0

    def park_car(self, car: Car):
        spot = self._parking_lot.park_car(car)
        if spot:
            self._current_car = car
            self._cars_served_today += 1
            print(f"{self.name} parked {car.owner_name}'s car at spot {spot}")

    def remove_car(self, spot_number: int):
        if spot_number in self._parking_lot.get_occupied_spots():
            car = self._parking_lot.occupied_spots[spot_number]
            self._parking_lot.remove_car(spot_number)
            if self._current_car == car:
                self._current_car = None
            print(f"{self.name} removed {car.owner_name}'s car from spot {spot_number}")
        else:
            print(f"{self.name}: no car found at spot {spot_number}")

    def get_free_spots(self):
        free = self._parking_lot.get_free_spots()
        print(f"{self.name} reports free spots: {free}")
        return free

    def reset_cars_served(self):
        print(f"{self.name} served {self._cars_served_today} cars today")
        self._cars_served_today = 0
