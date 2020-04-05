# test_port5_pytest.py

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

def test_sell():
    p = Portfolio()
    p.buy("MSFT", 100, 27.0)
    p.buy("DELL", 100, 17.0)
    p.buy("ORCL", 100, 34.0)
    p.sell("MSFT", 50)
    assert p.cost() == 6450

def test_not_enough():
    p = Portfolio()                 # Didn't I just do this?
    p.buy("MSFT", 100, 27.0)        #  |
    p.buy("DELL", 100, 17.0)        #  |
    p.buy("ORCL", 100, 34.0)        #  /
    with pytest.raises(ValueError):
        p.sell("MSFT", 200)

def test_dont_own_it():
    p = Portfolio()                 # What, again!?!?
    p.buy("MSFT", 100, 27.0)        #  |
    p.buy("DELL", 100, 17.0)        #  |
    p.buy("ORCL", 100, 34.0)        #  /
    with pytest.raises(ValueError):
        p.sell("IBM", 1)
