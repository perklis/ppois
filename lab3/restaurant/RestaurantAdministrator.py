from loyalty_system.Cashback import Cashback


class RestaurantAdministrator:
    def __init__(self, name: str):
        self.name = name
        self.__cashback_system = Cashback()
        self.__delivered_orders = []

    def confirm_delivery(self, client, order):
        print(f"Administrator {self.name} confirmed delivery for {client.name}")
        client.loyalty_card.add_cashback(order.price)
        self.__delivered_orders.append(order)

    def get_all_delivered_orders(self):
        return self.__delivered_orders
