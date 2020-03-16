"""
Patching an Object’s Attributes
Let’s say you only want to mock one method of an object instead of the entire object. You can do so by using patch.object().

For example, .test_get_holidays_timeout() really only needs to mock requests.get() and set its .side_effect to Timeout:

"""
import unittest
from my_calendar import requests, get_holidays
from unittest.mock import patch

class TestCalendar(unittest.TestCase):
    @patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout(self, mock_requests):
            with self.assertRaises(requests.exceptions.Timeout):
                get_holidays()

if __name__ == '__main__':
    unittest.main()