import random
import string


class PromocodeGenerator:
    def __init__(self):
        self._promocodes: dict[str, int] = {}
        self.generate_batch(7)

    def _generate_code(self, length: int = 8) -> str:
        return "".join(random.choices(string.ascii_letters, k=length))

    def generate_batch(self, count: int = 7):
        for i in range(count):
            code = self._generate_code()
            bonus = random.randint(5, 100)
            self._promocodes[code] = bonus
        print(f"Generated {count} promocodes")

    def get_bonus(self, code: str) -> int | None:
        return self._promocodes.get(code)

    def _show_all_codes(self):
        print("All promocodes:")
        for code, bonus in self._promocodes.items():
            print(f"{code}: {bonus}")
