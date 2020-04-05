# test_port6_pytest.py

import pytest

from portfolio2 import Portfolio

def test_empty():
    p = Portfolio()
    assert p.cost() == 0.0

def test_buy_one_stock():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    assert p.cost() == 17648.0

def test_buy_two_stocks():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    p.buy("HPQ", 100, 36.15)
    assert p.cost() == 21263.0

def test_bad_input():
    p = Portfolio()
    with pytest.raises(TypeError):
        p.buy("IBM")


@pytest.fixture
def simple_portfolio():
    p = Portfolio()
    p.buy("MSFT", 100, 27.0)
    p.buy("DELL", 100, 17.0)
    p.buy("ORCL", 100, 34.0)
    return p

def test_sell(simple_portfolio):
    simple_portfolio.sell("MSFT", 50)
    assert simple_portfolio.cost() == 6450

def test_not_enough(simple_portfolio):
    with pytest.raises(ValueError):
        simple_portfolio.sell("MSFT", 200)

def test_dont_own_it(simple_portfolio):
    with pytest.raises(ValueError):
        simple_portfolio.sell("IBM", 1)


# Tedious duplication:
def test_sell1(simple_portfolio):
    simple_portfolio.sell("MSFT", 50)
    assert simple_portfolio.cost() == 6450

def test_sell2(simple_portfolio):
    simple_portfolio.sell("MSFT", 10)
    assert simple_portfolio.cost() == 7530

def test_sell3(simple_portfolio):
    simple_portfolio.sell("ORCL", 90)
    assert simple_portfolio.cost() == 4740


# Nicely factored into parameters:
@pytest.mark.parametrize("sym, num, cost", [
    ("MSFT", 50, 6450),
    ("MSFT", 10, 7530),
    ("ORCL", 90, 4740),
])
def test_selling(simple_portfolio, sym, num, cost):
    simple_portfolio.sell(sym, num)
    assert simple_portfolio.cost() == cost
