from enum import StrEnum, auto


class PaymentStatus(StrEnum):
    PENDING = auto()
    COMPLETED = auto()
    FAILED = auto()
    REFUNDED = auto()
