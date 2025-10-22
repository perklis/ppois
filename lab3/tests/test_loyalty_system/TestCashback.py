import unittest
from loyalty_system.Cashback import Cashback
from loyalty_system.LoyaltyCard import LoyaltyCard


class TestCashback(unittest.TestCase):
    def setUp(self):
        self.cashback = Cashback(percent=5.0)
        self.loyalty_card = LoyaltyCard()

    def test_calculate(self):
        amount = self.cashback.calculate(200)
        self.assertEqual(amount, 10.0)

    def test_apply_to_card(self):
        self.cashback.apply_to_card(self.loyalty_card, 100)
        self.assertEqual(self.loyalty_card.get_balance(), 5.0)
