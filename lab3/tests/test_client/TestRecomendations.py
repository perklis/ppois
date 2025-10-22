import unittest
from unittest.mock import Mock
from client.Recomendations import Recomendations
from client.HistoryOfOrders import HistoryOfOrders


class TestRecomendations(unittest.TestCase):
    def setUp(self):
        self.history = Mock(spec=HistoryOfOrders)
        mock_order1 = Mock()
        mock_order2 = Mock()

        mock_order1.items = [
            Mock(food_item=Mock(), quantity=2),
            Mock(food_item=Mock(), quantity=3),
        ]
        mock_order1.items[0].food_item.name = "Pizza"
        mock_order1.items[1].food_item.name = "Banana"

        mock_order2.items = [
            Mock(food_item=Mock(), quantity=1),
            Mock(food_item=Mock(), quantity=1),
        ]
        mock_order2.items[0].food_item.name = "Pasta"
        mock_order2.items[1].food_item.name = "Pizza"

        self.history.get_all_orders.return_value = [mock_order1, mock_order2]
        self.recommender = Recomendations(self.history)

    def test_recommendations(self):
        result = self.recommender.get_recommendations(top_n=3)
        self.assertIn("Pizza", result)
        self.assertIn("Banana", result)
        self.assertTrue(len(result) <= 3)

    def test_empty_history(self):
        empty_history = Mock(spec=HistoryOfOrders)
        empty_history.get_all_orders.return_value = []
        recommender = Recomendations(empty_history)
        self.assertEqual(recommender.get_recommendations(), [])

    def test_limit(self):
        result = self.recommender.get_recommendations(top_n=1)
        self.assertEqual(len(result), 1)
