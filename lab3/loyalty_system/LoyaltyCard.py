from loyalty_system.LoyaltyCardGenerator import LoyaltyCardGenerator


class LoyaltyCard:
    def __init__(self):
        self.__card_number = LoyaltyCardGenerator.generate_card_number()
        self.__balance = 0.0

    def add_cashback(self, amount: float):
        self.__balance += amount
        print(f"{amount} added to loyalty card {self.__card_number}")

    def get_balance(self) -> float:
        print(f"Loyalty card balance: {self.__balance}")
        return self.__balance

    def get_card_number(self) -> str:
        return self.__card_number

    def __str__(self):
        return f"Loyalty Card {self.__card_number} (Balance: {self.__balance})"
