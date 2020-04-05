# test_port7_pytest.py

import pytest

from portfolio3 import Portfolio

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


@pytest.fixture
def fake_prices_portfolio(simple_portfolio):
    def fake_current_prices():
        return {'DELL': 140.0, 'ORCL': 32.0, 'MSFT': 51.0}
    simple_portfolio.current_prices = fake_current_prices
    return simple_portfolio

def test_value(fake_prices_portfolio):
    assert fake_prices_portfolio.value() == 22300
