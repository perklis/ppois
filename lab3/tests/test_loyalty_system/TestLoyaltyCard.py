import unittest
from loyalty_system.LoyaltyCard import LoyaltyCard


class TestLoyaltyCard(unittest.TestCase):
    def test_balance_and_unique_number(self):
        card1 = LoyaltyCard()
        card2 = LoyaltyCard()
        self.assertNotEqual(card1.get_card_number(), card2.get_card_number())
        card1.add_cashback(20)
        self.assertEqual(card1.get_balance(), 20)
        card1.add_cashback(5)
        self.assertEqual(card1.get_balance(), 25)
