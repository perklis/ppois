import unittest
from unittest.mock import Mock
from delivery.DeliveryEstimator import DeliveryEstimator
from orders.Order import Order
from delivery.courier.Courier import Courier


class TestDeliveryEstimator(unittest.TestCase):
    def setUp(self):
        self.estimator = DeliveryEstimator()
        self.mock_order = Mock(spec=Order)
        self.mock_order.order_number = 1
        self.mock_order.items = [Mock(), Mock()]
        self.mock_order.client = Mock()
        self.mock_order.client._address.city = "Minsk"

        self.courier1 = Mock(spec=Courier)
        self.courier1.on_shift = True
        self.courier1.status = "waiting"
        self.courier1.salary = 50
        self.courier1.name = "Goga"

        self.courier2 = Mock(spec=Courier)
        self.courier2.on_shift = True
        self.courier2.status = "waiting"
        self.courier2.salary = 40
        self.courier2.name = "Tolik"

    def test_estimate_time(self):
        time = self.estimator.estimate_time(self.mock_order)
        self.assertEqual(time, 10 + len(self.mock_order.items) * 5)

    def test_estimate_cost_no_weather_increase(self):
        self.estimator.weather.get_weather = Mock(return_value="sunny")
        cost = self.estimator.estimate_cost(self.mock_order)
        expected_cost = 3 + len(self.mock_order.items) * 1.5
        self.assertEqual(cost, expected_cost)

    def test_estimate_cost_with_weather_increase(self):
        self.estimator.weather.get_weather = Mock(return_value="snow")
        cost = self.estimator.estimate_cost(self.mock_order)
        expected_cost = (3 + len(self.mock_order.items) * 1.5) * 1.03
        self.assertAlmostEqual(cost, round(expected_cost, 2))

    def test_assign_courier_selects_lowest_salary(self):
        selected = self.estimator.assign_courier(
            self.mock_order, [self.courier1, self.courier2]
        )
        self.assertEqual(selected, self.courier2)

    def test_assign_courier_raises_if_none_available(self):
        self.courier1.on_shift = False
        self.courier2.on_shift = False
        with self.assertRaises(Exception):
            self.estimator.assign_courier(
                self.mock_order, [self.courier1, self.courier2]
            )
