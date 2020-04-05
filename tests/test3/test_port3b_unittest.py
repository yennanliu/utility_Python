# test_port3b.py

import unittest
from portfolio1 import Portfolio

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
