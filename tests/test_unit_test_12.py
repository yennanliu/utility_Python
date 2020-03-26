"""
* Patching an Object’s Attributes

Let’s say you only want to mock one method of an object 
instead of the entire object. You can do so by using patch.object().

For example, .test_get_holidays_timeout() really only needs to mock requests.get() and set its .side_effect to Timeout:
"""
import unittest
from unittest.mock import patch, Mock
from my_db_utils import get_db_conn, sqlalchemy
from sqlalchemy.exc import DatabaseError


class TestMyFunc(unittest.TestCase):

    @patch.object(sqlalchemy, 'create_engine', side_effect=sqlalchemy.exc.ArgumentError)
    def test_get_db_conn(self, mock_sqlalchemy):

        if self.assertRaises(sqlalchemy.exc.ArgumentError):
            get_db_conn()


if __name__ == '__main__':
    unittest.main()
