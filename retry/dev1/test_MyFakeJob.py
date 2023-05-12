import datetime as dt
#from BackfillOperator import backfill_operator
from MyFakeJob import MyFakeETL
import pytest
#from unittest import TestCase

def run_raise_exception_null_input():
    etl = MyFakeETL(1,2,3)
    etl.run_etl()


def test_raise_exception_null_input():
    with pytest.raises(ValueError):
        etl = MyFakeETL(1,2,3)
        etl.run_etl()

def my_func(x):
    if x < 0:
        raise ValueError("TO SMALL!!")

def greet(greeting):
    if greeting not in ('hello', 'hi'):
        raise ValueError(f'{greeting} is not allowed')
    
    print(greeting + ' world!')

def test_greet():
    with pytest.raises(ValueError):
        greet('bye')

def test_my_func():
    with pytest.raises(ValueError):
        my_func(-1)

# if __name__ == '__main__':
#     print ("test_greet")
#     test_greet()