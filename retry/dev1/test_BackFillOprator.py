import datetime as dt
from BackfillOperator import backfill_operator
import pytest


def test_should_raise_exception_if_func_return_null():

    @backfill_operator(max_run=10)
    def my_dummy_func():
        return None

    with pytest.raises(TypeError):
        my_dummy_func()


def test_should_raise_exception_if_func_return_type_wrong():

    @backfill_operator(max_run=10)
    def my_dummy_func():
        return 123

    with pytest.raises(TypeError):
        my_dummy_func()

def test_should_raise_exception_if_func_return_has_no_return():

    @backfill_operator(max_run=10)
    def my_dummy_func():
        print(123)

    with pytest.raises(TypeError):
        my_dummy_func()

def test_should_raise_exception_if_backfill_operator_with_wrong_param_type():

    @backfill_operator(max_run=10, 
        min_data_lag_to_stop=1000, 
        latest_time_for_rerun=dt.timedelta(seconds=1 + 1))
    def my_dummy_func():
        return dt.timedelta(seconds=1 + 1)

    with pytest.raises(TypeError):
        my_dummy_func()

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
