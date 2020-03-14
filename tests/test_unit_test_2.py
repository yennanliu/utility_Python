"""
modify from 
https://realpython.com/python-mock-library/#patch
"""
import unittest
from mydevclass.my_calendar import is_weekday
from requests.exceptions import Timeout
from unittest.mock import patch, Mock
import datetime
import pytest

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# def is_weekday():
#     today = datetime.datetime.today()
#     # Python's datetime library treats Monday as 0 and Sunday as 6
#     return (0 <= today.weekday() < 5)

def test_is_weekday():
    # Mock datetime to control today's date
    datetime = Mock()

    ### Mock .today() to return Tuesday ###
    datetime.datetime.today.return_value = tuesday
    # Test Tuesday is a weekday
    #print ("is_weekday()", is_weekday())
    assert (is_weekday() == False)

    ###  Mock .today() to return Saturday ###
    datetime.datetime.today.return_value = saturday
    # Test Saturday is not a weekday
    assert not (is_weekday() == True)
