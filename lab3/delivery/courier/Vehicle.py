class Vehicle:
    def __init__(self, type_name: str, number_plate: str = ""):
        self.type_name = type_name
        self.number_plate = number_plate

    def show_vehicle(self):
        if self.number_plate:
            print(f"Vehicle: {self.type_name}, Plate: {self.number_plate}")
        else:
            print(f"Vehicle: {self.type_name}")
