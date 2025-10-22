class Addres:
    def __init__(self, street: str, city: str, house_or_flat_number: int):
        self.street = street
        self.city = city
        self.house_or_flat_number = house_or_flat_number

    def full_address(self):
        return f"{self.street}, {self.city}, {self.house_or_flat_number}"
