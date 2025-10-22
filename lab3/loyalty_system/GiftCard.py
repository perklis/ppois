from datetime import datetime
from exceptions import GiftCardNotFound


class GiftCard:
    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        self.issued_at = datetime.now()
        self.active = True

    def use(self):
        if not self.active:
            raise GiftCardNotFound("GiftCard doesn't found")
        self.active = False
        print(f"GiftCard used by {self.owner_name}")
