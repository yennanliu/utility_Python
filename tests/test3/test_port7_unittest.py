# test_port7_unittest.py

import unittest
from portfolio3 import Portfolio

class PortfolioTest(unittest.TestCase):
    def test_empty(self):
        p = Portfolio()
        self.assertEqual(p.cost(), 0.0)

    def test_buy_one_stock(self):
        p = Portfolio()
        p.buy("IBM", 100, 176.48)
        self.assertEqual(p.cost(), 17648.0)

    def test_buy_two_stocks(self):
        p = Portfolio()
        p.buy("IBM", 100, 176.48)
        p.buy("HPQ", 100, 36.15)
        self.assertEqual(p.cost(), 21263.0)

    def test_bad_input(self):
        p = Portfolio()
        with self.assertRaises(TypeError):
            p.buy("IBM")


class PortfolioSellTest(unittest.TestCase):
    def setUp(self):
        self.p = Portfolio()
        self.p.buy("MSFT", 100, 27.0)
        self.p.buy("DELL", 100, 17.0)
        self.p.buy("ORCL", 100, 34.0)

    def test_sell(self):
        self.p.sell("MSFT", 50)
        self.assertEqual(self.p.cost(), 6450)

    def test_not_enough(self):
        with self.assertRaises(ValueError):
            self.p.sell("MSFT", 200)

    def test_dont_own_it(self):
        with self.assertRaises(ValueError):
            self.p.sell("IBM", 1)


# Replace Portfolio.current_prices with a stub implementation.
# This avoids the web, but also skips all our current_prices
# code.
class PortfolioValueTest(unittest.TestCase):
    def fake_current_prices(self):
        return {'IBM': 140.0, 'HPQ': 32.0}

    def setUp(self):
        self.p = Portfolio()
        self.p.buy("IBM", 100, 120.0)
        self.p.buy("HPQ", 100, 30.0)
        self.p.current_prices = self.fake_current_prices

    def test_value(self):
        self.assertEqual(self.p.value(), 17200)
