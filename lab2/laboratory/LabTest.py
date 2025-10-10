class LabTest:
    def __init__(self, test_name: str, normal_range: str, units: str):
        self.test_name = test_name
        self.normal_range = normal_range 
        self.units = units

    def __str__(self):
        return f"{self.test_name} (Normal: {self.normal_range} {self.units})"
