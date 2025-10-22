from orders.Order import Order
from orders.OrderItem import OrderItem
from delivery.DeliveryZone import DeliveryZone
from exceptions import AdressNotInDeliveryZone, EmptyClientWishlistError
from payment.PaymentBy import PaymentBy
from client.Client import Client


class CallCenter:
    def __init__(self, name: str):
        self.name = name

    def receive_call(self, client: Client):
        print(f"Call from {client.name} received by {self.name}")

    def take_order(self, client: Client):
        if not client._wishlist:
            raise EmptyClientWishlistError("Wishlist is empty")

        zone = DeliveryZone()
        if not zone.is_in_zone(client._address):
            raise AdressNotInDeliveryZone(
                f"Delivery is not available for {client._address.street}."
            )

        order = Order(client)
        for dish in client._wishlist:
            order.add_item(OrderItem(dish, 1))

        client._wishlist.clear()
        print(f"Order created for {client.name} by CallCenter {self.name}")

        if client.gift_card and client.gift_card.active:
            order.pay(PaymentBy.GIFTCARD)
            client.gift_card.use()
        else:
            order.pay()

        return order
