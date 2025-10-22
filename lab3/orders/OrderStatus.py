from enum import StrEnum, auto


class OrderStatus(StrEnum):
    PROCESSING = auto()
    READY = auto()
    ON_THE_WAY = auto()
    DELIVERED = auto()
