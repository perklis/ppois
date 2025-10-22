from loyalty_system.Promocode import Promocode
from loyalty_system.LoyaltyCard import LoyaltyCard
from delivery.DeliveryEmployee import DeliveryEmployee


class DeliveryAdministrator(DeliveryEmployee):
    def __init__(
        self,
        name: str,
        phone: str,
        salary: float,
        experience: int,
        department: str,
        promocode_system: Promocode,
    ):
        super().__init__(name, phone, salary, experience, department)
        self.__promocode_system = promocode_system

    def confirm_delivery(self, order, courier, loyalty_card: LoyaltyCard):
        if order.status != "delivered":
            print(f"Order {order.order_number} not yet delivered")
            return

        courier.complete_task()
        courier.salary += 5
        print(f"Courier {courier.name} received +5 to salary")

        active_code = self.__promocode_system.get_active_code()
        if active_code:
            bonus = self.__promocode_system.get_bonus_amount()
            loyalty_card.add_cashback(bonus)
            print(f"Bonus {bonus} added promocode {active_code}")

    def get_promocode_system(self):
        return self.__promocode_system

    def __str__(self):
        return f"Delivery Administrator {self.name} ({self.department})"
