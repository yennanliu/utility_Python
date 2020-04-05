# test_port1_pytest.py

from portfolio1 import Portfolio

def test_buy_one_stock():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    assert p.cost() == 17648.0
