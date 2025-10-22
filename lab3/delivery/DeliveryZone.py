class DeliveryZone:
    def __init__(self):
        self.__available_streets = {
            "Lenina",
            "Petrova",
            "Bedy",
            "Solnechnaya",
            "Pushkina",
            "Sovetskaya",
            "Kirova",
            "Sadovaya",
            "Gagarina",
            "Zelenaya",
        }

    def is_in_zone(self, address) -> bool:
        return address.street in self.__available_streets

    def add_street(self, street: str):
        self.__available_streets.add(street)
        print(f"Street {street} added to delivery zone")

    def remove_street(self, street: str):
        if street in self.__available_streets:
            self.__available_streets.remove(street)
            print(f"Street {street} removed from delivery zone")

    def list_streets(self):
        print("Available delivery streets:")
        for s in sorted(self.__available_streets):
            print(f"- {s}")
