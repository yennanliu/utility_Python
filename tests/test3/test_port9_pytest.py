# test_port9_pytest.py

from types import SimpleNamespace

import pytest

from portfolio3 import Portfolio
import portfolio3

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


def test_value(simple_portfolio, mocker):
    req_get = mocker.patch(
        "portfolio3.requests.get",
        return_value=SimpleNamespace(
            text='\nDELL,,,140\nORCL,,,32\nMSFT,,,51\n'
        ),
    )
    assert simple_portfolio.value() == 22300

    assert len(req_get.call_args_list) == 1
    opened_url = req_get.call_args_list[0][0][0]
    assert "api.worldtradingdata.com/api/v1/stock" in opened_url
    assert "symbol=DELL,MSFT,ORCL" in opened_url
