from loyalty_system.LoyaltyCard import LoyaltyCard
from loyalty_system.PromocodeGenerator import PromocodeGenerator
from exceptions import InvalidPromocode


class Promocode:
    def __init__(self, generator: PromocodeGenerator):
        self.__generator = generator
        self.__active_code: str | None = None
        self.__bonus_amount: int = 0

    def activate(self, code: str, loyalty_card: LoyaltyCard):
        if self.__active_code:
            raise InvalidPromocode("Promocode already activated")

        bonus = self.__generator.get_bonus(code)
        if bonus is None:
            raise InvalidPromocode("Promocode doesn't exist")

        loyalty_card.add_cashback(bonus)
        self.__active_code = code
        self.__bonus_amount = bonus
        print(f"Promocode {code} activated, {bonus} added")

    def get_active_code(self) -> str | None:
        return self.__active_code

    def get_bonus_amount(self) -> int:
        return self.__bonus_amount
