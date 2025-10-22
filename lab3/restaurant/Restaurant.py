from restaurant.kitchen.Cook import Cook
from restaurant.kitchen.Shef import Shef
from restaurant.Menu import Menu
from restaurant.Picker import Picker
from orders.Order import Order
from restaurant.kitchen.OrderQueue import OrderQueue
from restaurant.RestaurantRating import RestaurantRating
from restaurant.WorkingTime import WorkingTime
from restaurant.RestaurantAnalytics import RestaurantAnalytics
from delivery.courier.Courier import Courier
from client.Client import Client


class Restaurant:
    def __init__(self, name: str):
        self.name = name
        self.menu = Menu()
        self.queue = OrderQueue()
        self.rating = RestaurantRating()
        self.working_time = WorkingTime(name)
        self.analytics = RestaurantAnalytics()
        self.cooks: list[Cook] = []
        self.shef: Shef | None = None
        self.pickers: list[Picker] = []
        self.couriers: list[Courier] = []

    def add_shef(self, shef: Shef):
        self.shef = shef
        print(f"Added Shef {shef.name} to {self.name}")

    def add_cook(self, cook: Cook):
        self.cooks.append(cook)
        print(f"Added Cook {cook.name} to {self.name}")

    def add_picker(self, picker: Picker):
        self.pickers.append(picker)
        print(f"Added Picker {picker.name} to {self.name}")

    def add_courier(self, courier: Courier):
        self.couriers.append(courier)
        print(f"Added Courier {courier.name} to {self.name}")

    def receive_order(self, order: Order, client: Client):
        self.queue.add_order(order)
        self.analytics.record_order(order)
        print(
            f"Restaurant {self.name} received order #{order.order_number} from {client.name}"
        )

    def process_next_order(self):
        courier = None
        for courier in self.couriers:
            if courier.status == "waiting" and courier.current_order is None:
                courier = courier
                break
        order = self.queue.next_order(courier)
        if order:
            print(f"Processing order #{order.order_number}")
        return order

    def show_menu(self):
        self.menu.show_menu()

    def add_rating(self, order: Order, value: float):
        self.rating.add_rating(order, value)
