# test_port5_unittest.py

import unittest
from portfolio2 import Portfolio

class PortfolioTestCase(unittest.TestCase):
    """Base class for all Portfolio tests."""

    def assertCostEqual(self, p, cost):
        """Assert that `p`'s cost is equal to `cost`."""
        self.assertEqual(p.cost(), cost)


class PortfolioTest(PortfolioTestCase):
    def test_empty(self):
        p = Portfolio()
        self.assertCostEqual(p, 0.0)

    def test_buy_one_stock(self):
        p = Portfolio()
        p.buy("IBM", 100, 176.48)
        self.assertCostEqual(p, 17648.0)

    def test_buy_two_stocks(self):
        p = Portfolio()
        p.buy("IBM", 100, 176.48)
        p.buy("HPQ", 100, 36.15)
        self.assertCostEqual(p, 21263.0)

    def test_bad_input(self):
        p = Portfolio()
        with self.assertRaises(TypeError):
            p.buy("IBM")


class PortfolioSellTest(PortfolioTestCase):
    def test_sell(self):
        p = Portfolio()
        p.buy("MSFT", 100, 27.0)
        p.buy("DELL", 100, 17.0)
        p.buy("ORCL", 100, 34.0)
        p.sell("MSFT", 50)
        self.assertCostEqual(p, 6450)

    def test_not_enough(self):
        p = Portfolio()             # Didn't I just do this?
        p.buy("MSFT", 100, 27.0)
        p.buy("DELL", 100, 17.0)
        p.buy("ORCL", 100, 34.0)
        with self.assertRaises(ValueError):
            p.sell("MSFT", 200)

    def test_dont_own_it(self):
        p = Portfolio()             # What, again!?!?
        p.buy("MSFT", 100, 27.0)
        p.buy("DELL", 100, 17.0)
        p.buy("ORCL", 100, 34.0)
        with self.assertRaises(ValueError):
            p.sell("IBM", 1)
