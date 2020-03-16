"""
patch() as a Context Manager
Sometimes, you’ll want to use patch() as a context manager rather than a decorator. Some reasons why you might prefer a context manager include the following:

You only want to mock an object for a part of the test scope.
You are already using too many decorators or parameters, which hurts your test’s readability.
To use patch() as a context manager, you use Python’s with statement:

"""
import unittest
from my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch

class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        with patch('my_calendar.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

if __name__ == '__main__':
    unittest.main()