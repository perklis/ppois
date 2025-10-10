from typing import Dict, List, Optional
from parking.Car import Car


class Parking:
    def __init__(
        self, lot_name: str, total_spots: int, has_electric_charging: bool = False
    ):
        self.lot_name = lot_name
        self.total_spots = total_spots
        self.has_electric_charging = has_electric_charging
        self.occupied_spots: Dict[int, Car] = {}

    def park_car(self, car: Car) -> Optional[int]:
        for spot in range(1, self.total_spots + 1):
            if spot not in self.occupied_spots:
                self.occupied_spots[spot] = car
                print(f"{car.owner_name}'s car parked at spot {spot}")
                return spot
        print(f"No available spots to park {car.owner_name}'s car")
        return None

    def remove_car(self, spot_number: int):
        if spot_number in self.occupied_spots:
            car = self.occupied_spots.pop(spot_number)
            print(f"{car.owner_name}'s car removed from spot {spot_number}")
        else:
            print(f"No car found at spot {spot_number}")

    def get_free_spots(self) -> List[int]:
        return [
            spot
            for spot in range(1, self.total_spots + 1)
            if spot not in self.occupied_spots
        ]

    def get_occupied_spots(self) -> Dict[int, Car]:
        return self.occupied_spots
