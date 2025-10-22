import unittest
from unittest.mock import Mock
from delivery.Delivery import Delivery
from delivery.courier.Courier import Courier
from orders.Order import Order


class TestDelivery(unittest.TestCase):
    def setUp(self):
        self.delivery_system = Delivery()
        self.mock_courier = Mock(spec=Courier)
        self.mock_courier.name = "John"
        self.mock_courier.current_order = None
        self.mock_courier.take_order = Mock()
        self.mock_courier.deliver_order = Mock()
        self.mock_courier.status = "waiting"
        self.delivery_system.add_courier(self.mock_courier)

        self.mock_order = Mock(spec=Order)
        self.mock_order.order_number = 1
        self.mock_order.items = ["item1", "item2"]
        self.delivery_system.estimator.assign_courier = Mock(
            return_value=self.mock_courier
        )

    def test_add_courier(self):
        courier2 = Mock(spec=Courier)
        courier2.name = "Anna"
        self.delivery_system.add_courier(courier2)
        self.assertIn(courier2, self.delivery_system.couriers)

    def test_assign_order(self):
        self.delivery_system.assign_order(self.mock_order)
        self.mock_courier.take_order.assert_called_once_with(self.mock_order.items)
        self.assertIn(self.mock_order, self.delivery_system.orders_in_progress)

    def test_assign_order_no_courier(self):
        self.delivery_system.estimator.assign_courier.return_value = None
        order2 = Mock(spec=Order)
        order2.order_number = 2
        order2.items = ["itemA"]
        self.delivery_system.assign_order(order2)
        self.assertNotIn(order2, self.delivery_system.orders_in_progress)

    def test_complete_order(self):
        self.mock_courier.current_order = [Mock()]
        self.delivery_system.orders_in_progress.append(self.mock_order)

        self.delivery_system.complete_order(self.mock_courier, customer_rating=4)
        self.mock_courier.deliver_order.assert_called_once_with(customer_rating=4)
