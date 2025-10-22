from enum import StrEnum, auto


class PaymentBy(StrEnum):
    CASH = auto()
    CARD = auto()
    ONLINE = auto()
    GIFTCARD = auto()
