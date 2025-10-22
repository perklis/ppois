from __future__ import annotations
from datetime import datetime
from typing import List, Dict, Any
from exceptions import OrderNotFound


class HistoryOfOrders:
    def __init__(self, client_name: str):
        self.__client_name: str = client_name
        self.__orders: List[Dict[str, Any]] = []

    def add_order(self, order: "Order") -> None:
        record = {"order": order, "time": datetime.now()}
        self.__orders.append(record)
        print(f"Order added for {self.__client_name}")

    def get_all_orders(self) -> List["Order"]:
        return [r["order"] for r in self.__orders]

    def get_last_order(self) -> "Order":
        if not self.__orders:
            raise OrderNotFound(f"No orders for {self.__client_name}")
        return self.__orders[-1]["order"]

    def count_orders(self) -> int:
        return len(self.__orders)

    def get_total_spent(self) -> float:
        total = sum(r["order"].get_total_price() for r in self.__orders)
        print(f"Total spent by {self.__client_name} is {total}")
        return total
