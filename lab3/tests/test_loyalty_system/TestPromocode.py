import unittest
from loyalty_system.LoyaltyCard import LoyaltyCard
from loyalty_system.Promocode import Promocode
from loyalty_system.PromocodeGenerator import PromocodeGenerator


class TestPromocode(unittest.TestCase):
    def setUp(self):
        self.generator = PromocodeGenerator()
        self.loyalty_card = LoyaltyCard()
        self.promocode = Promocode(self.generator)

    def test_activate_valid_code(self):
        code = list(self.generator._promocodes.keys())[0]
        bonus = self.generator.get_bonus(code)
        self.promocode.activate(code, self.loyalty_card)
        self.assertEqual(self.promocode.get_active_code(), code)
        self.assertEqual(self.promocode.get_bonus_amount(), bonus)
        self.assertEqual(self.loyalty_card.get_balance(), bonus)

    def test_activate_invalid_code_raises(self):
        with self.assertRaises(Exception):
            self.promocode.activate("INVALID", self.loyalty_card)

    def test_activate_twice_raises(self):
        code = list(self.generator._promocodes.keys())[0]
        self.promocode.activate(code, self.loyalty_card)
        with self.assertRaises(Exception):
            self.promocode.activate(code, self.loyalty_card)
