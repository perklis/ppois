from __future__ import annotations
from client.Addres import Addres
from client.HistoryOfOrders import HistoryOfOrders
from client.Weather import Weather
from restaurant.Menu import Menu
from orders.Order import Order
from orders.OrderItem import OrderItem
from delivery.DeliveryZone import DeliveryZone
from exceptions import AdressNotInDeliveryZone, EmptyClientWishlistError
from payment.PaymentBy import PaymentBy
from loyalty_system.GiftCard import GiftCard


class Client:
    def __init__(self, name: str, phone: str, address: Addres):
        self.name = name
        self.phone = phone
        self._address = address
        self.__order_history = HistoryOfOrders(self.name)
        self.__weather = Weather()
        self._wishlist = []
        self.gift_card: GiftCard | None = None

    def browse_menu(self, menu: Menu):
        menu.show_menu()

    def view_category(self, menu: Menu, category_name: str):
        dishes = menu.find_by_category(category_name)
        if dishes:
            print(f"\n{category_name}")
            for d in dishes:
                print(f"{d.name} {d.price}")

    def add_to_wishlist(self, food_item):
        self._wishlist.append(food_item)
        print(f"Added {food_item.name} to wishlist")

    def remove_from_wishlist(self, dish_name: str):
        self._wishlist = [d for d in self._wishlist if d.name != dish_name]
        print(f"Removed {dish_name} from wishlist")

    def show_wishlist(self):
        print("Wishlist:")
        for d in self._wishlist:
            print(f"{d.name} — {d.price}")

    def call_center(self, call_center: "CallCenter"):
        print(f"{self.name} is calling CallCenter {call_center.name}")
        call_center.receive_call(self)
        order = call_center.take_order(self)
        print(f"Order successfully created by CallCenter for {self.name}")
        return order

    def buy_gift_card(self):
        if self.gift_card and self.gift_card.active:
            print("You already have GiftCard")
            return
        self.gift_card = GiftCard(self.name)
        print(f"{self.name} bought gift card")

    def make_order(self):
        if not self._wishlist:
            raise EmptyClientWishlistError("Wishlist is empty, nothing to order")

        zone = DeliveryZone()
        if not zone.is_in_zone(self._address):
            raise AdressNotInDeliveryZone(
                f"Delivery is not available for {self._address.street}."
            )

        order = Order(self)
        for dish in self._wishlist:
            order.add_item(OrderItem(dish, 1))

        self._wishlist.clear()
        self.__order_history.add_order(order)

        if self.gift_card and self.gift_card.active:
            order.pay(PaymentBy.GIFTCARD)
            self.gift_card.use()
        else:
            order.pay()

        print(f"Order successfully created for {self.name}")
        return order

    def get_order_history(self):
        return self.__order_history.get_all_orders()

    def get_last_order(self):
        return self.__order_history.get_last_order()

    def get_total_orders(self):
        return self.__order_history.count_orders()

    def get_total_spent(self):
        return self.__order_history.get_total_spent()

    def update_address(self, new_address: Addres):
        self._address = new_address
        print(f"ℹ{self.name} updated address to {new_address.full_address()}")

    def check_weather(self):
        return self.__weather.get_weather(self._address.city)
