from typing import List, Dict
from client.HistoryOfOrders import HistoryOfOrders


class Recomendations:
    def __init__(self, order_history: HistoryOfOrders):
        self.order_history = order_history

    def get_recommendations(self, top_n: int = 5) -> List[str]:
        frequency: Dict[str, int] = {}

        for order in self.order_history.get_all_orders():
            for item in order.items:
                name = item.food_item.name
                quantity = item.quantity
                if name in frequency:
                    frequency[name] += quantity
                else:
                    frequency[name] = quantity

        items_list = list(frequency.items())
        items_count = len(items_list)
        for i in range(items_count):
            for j in range(i + 1, items_count):
                if items_list[i][1] < items_list[j][1]:
                    items_list[i], items_list[j] = items_list[j], items_list[i]

        recommended = []
        for i in range(min(top_n, items_count)):
            recommended.append(items_list[i][0])

        print(f"Recommended products: {', '.join(str(x) for x in recommended)}")
        return recommended
