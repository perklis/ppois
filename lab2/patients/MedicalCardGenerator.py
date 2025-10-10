import random


class MedicalCardGenerator:
    def __init__(self, start_symbols: str = "MC"):
        self.start_symbols = start_symbols
        self.generated_numbers = set()

    def generate(self, birth_year: int | None = None) -> str:
        while True:
            random_number = random.randint(1000, 9999)
            number = f"{self.start_symbols}{birth_year or ''}{random_number}"
            if number not in self.generated_numbers:
                self.generated_numbers.add(number)
                return number
