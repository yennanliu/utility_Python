# portfolio3.py

import csv

import requests


class Portfolio:
    """A simple stock portfolio

    >>> p = Portfolio()
    >>> p.cost()
    0.0

    >>> p.buy("IBM", 100, 176.48)
    >>> p.cost()
    17648.0

    >>> p.buy("HPQ", 100, 36.15)
    >>> p.cost()
    21263.0

    """
    def __init__(self):
        # A list of lists: [[name, shares, price], ...]
        self.stocks = []

    def buy(self, name, shares, price):
        """Buy shares at a certain price."""
        self.stocks.append([name, shares, price])

    def cost(self):
        """What was the total cost of this portfolio?"""
        amt = 0.0
        for name, shares, price in self.stocks:
            amt += shares * price
        return amt

    def sell(self, name, shares):
        """Sell some number of shares of `name`."""
        for holding in self.stocks:
            if holding[0] == name:
                if holding[1] < shares:
                    raise ValueError("Not enough shares")
                holding[1] -= shares
                break
        else:
            raise ValueError("You don't own that stock")

    SUFFIX = "&api_token=C5He7fxdnYvFGH2rJHRV47XRzYVjUxkdFPRaVM9ILMvlsoSAmqbggY3VbPgG&output=csv"

    def current_prices(self):
        """Return a dict mapping names to current prices."""
        url = "https://api.worldtradingdata.com/api/v1/stock?symbol="
        url += ",".join(s[0] for s in sorted(self.stocks))
        url += self.SUFFIX
        data = requests.get(url).text
        lines = data.splitlines()[1:]
        return { row[0]: float(row[3]) for row in csv.reader(lines) }

    def value(self):
        """Return the current value of the portfolio."""
        prices = self.current_prices()
        total = 0.0
        for name, shares, _ in self.stocks:
            total += shares * prices[name]
        return total
