# test_port4_pytest_broken.py

from portfolio1 import Portfolio

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
    p.buy("IBM")
