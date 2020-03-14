"""
modify from 
https://realpython.com/python-mock-library/#patch
"""
import unittest
from requests.exceptions import Timeout
from unittest.mock import patch, Mock
import pytest

# Mock requests to control its behavior
requests = Mock()

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        ### set up side_effect ### ( side_effect : what will happen when call the method)
        # Test a connection timeout
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

if __name__ == '__main__':
    unittest.main()
