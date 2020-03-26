"""
* use patch() as a context manager rather than a decorator

same test as test_unit_test_10.py with different form (patch() as a Context Manager)
some reasons when do in this way:
	- You only want to mock an object for a part of the test scope.
	- You are already using too many decorators or parameters, which hurts your test’s readability.
"""
import unittest
from unittest.mock import patch, Mock
from my_db_utils import get_db_conn, sqlalchemy
from sqlalchemy.exc import DatabaseError


class TestMyFunc(unittest.TestCase):

    def test_get_db_conn(self):
    	with patch('my_db_utils.sqlalchemy') as mock_sqlalchemy:
	        mock_sqlalchemy.create_engine.side_effect = DatabaseError
	        mock_sqlalchemy.get_conn.return_value = "db_conn"
	        get_db_conn()
	        
	        mock_sqlalchemy.create_engine.assert_called_once()
	        assert mock_sqlalchemy.get_conn() == "db_conn"


if __name__ == '__main__':
    unittest.main()
