class HeadException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg: str = msg


class NotEnoughInStock(HeadException): ...


class InvalidPromocode(HeadException): ...


class AdressNotInDeliveryZone(HeadException): ...


class EmptyClientWishlistError(HeadException): ...


class OrderNotFound(HeadException): ...


class CleaningError(HeadException): ...


class GiftCardNotFound(HeadException): ...


class RatingInputError(HeadException): ...


class EmptyOrderQueue(HeadException): ...


class CouriersNotFound(HeadException): ...


class RatingTypeError(HeadException): ...


class DishesNotFoundError(HeadException): ...
