import random


class LoyaltyCardGenerator:
    _issued_cards = set()

    @classmethod
    def generate_card_number(cls) -> str:
        while True:
            digits = "".join(str(random.randint(0, 9)) for i in range(6))
            card_number = f"LC{digits}"
            if card_number not in cls._issued_cards:
                cls._issued_cards.add(card_number)
                return card_number
